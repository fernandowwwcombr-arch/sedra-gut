"""
Testes automáticos das rotas principais do SEDRA GUT.
"""

import pytest
from werkzeug.security import generate_password_hash
from app import app as flask_app
from database import db, Usuario, Categoria


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    flask_app.config["WTF_CSRF_ENABLED"] = False
    flask_app.config["SECRET_KEY"] = "test-secret"

    with flask_app.app_context():
        db.create_all()
        # Admin de teste
        admin = Usuario(
            nome="Admin Teste",
            email="admin@teste.com",
            senha_hash=generate_password_hash("senha123"),
            perfil="administrador",
            ativo=True,
        )
        db.session.add(admin)
        # Categoria padrão
        db.session.add(Categoria(nome="Geral", ativa=True, criado_por="sistema"))
        db.session.commit()
        yield flask_app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def cliente_logado(client):
    client.post("/login", data={"email": "admin@teste.com", "senha": "senha123"})
    return client


# ── Rotas públicas ─────────────────────────────────────────────

def test_raiz_redireciona_para_login(client):
    r = client.get("/")
    assert r.status_code == 302
    assert "/login" in r.headers["Location"]


def test_login_pagina_abre(client):
    r = client.get("/login")
    assert r.status_code == 200


def test_login_credenciais_erradas(client):
    r = client.post("/login", data={"email": "x@x.com", "senha": "errada"})
    assert r.status_code == 200
    assert "incorretos" in r.data.decode("utf-8")


def test_login_sucesso_redireciona_dashboard(client):
    r = client.post(
        "/login",
        data={"email": "admin@teste.com", "senha": "senha123"},
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "dashboard" in r.request.path


# ── Rotas protegidas ───────────────────────────────────────────

def test_dashboard_sem_login_redireciona(client):
    r = client.get("/dashboard")
    assert r.status_code == 302
    assert "/login" in r.headers["Location"]


def test_dashboard_com_login_abre(cliente_logado):
    r = cliente_logado.get("/dashboard")
    assert r.status_code == 200


# ── Criação de tarefa ──────────────────────────────────────────

def test_criar_tarefa_gut_valido(cliente_logado):
    r = cliente_logado.post(
        "/tarefa/nova",
        data={
            "titulo": "Tarefa de teste",
            "descricao": "Descrição",
            "responsavel": "Fulano",
            "categoria": "Geral",
            "gravidade": "5",
            "urgencia": "4",
            "tendencia": "3",
        },
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "Tarefa de teste" in r.data.decode("utf-8")


def test_criar_tarefa_sem_titulo_rejeita(cliente_logado):
    r = cliente_logado.post(
        "/tarefa/nova",
        data={
            "titulo": "",
            "gravidade": "1",
            "urgencia": "1",
            "tendencia": "1",
        },
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "obrigatório" in r.data.decode("utf-8")


# ── Score GUT ──────────────────────────────────────────────────

def test_score_gut_maximo():
    from database import Tarefa
    t = Tarefa(gravidade=5, urgencia=5, tendencia=5, prioridade=125, titulo="x")
    assert t.nivel_prioridade() == ("Crítica", "danger")


def test_score_gut_baixo():
    from database import Tarefa
    t = Tarefa(gravidade=1, urgencia=1, tendencia=1, prioridade=1, titulo="x")
    assert t.nivel_prioridade() == ("Baixa", "secondary")
