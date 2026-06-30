# SEDRA GUT — V1.0626
## Sistema de Priorização de Tarefas com Matriz GUT

---

## 📋 O que é este aplicativo?

O **SEDRA GUT** permite cadastrar e priorizar tarefas usando a **Matriz GUT**:
- **G**ravidade: qual o impacto se o problema não for resolvido? (1 a 5)
- **U**rgência: qual o prazo disponível para resolver? (1 a 5)
- **T**endência: como o problema evolui sem ação? (1 a 5)
- **Prioridade = G × U × T** (máximo: 125 pontos)

---

## 🚀 Como instalar e rodar

### Pré-requisitos
- Python 3.10 ou superior instalado
- Acesso ao terminal (Prompt de Comando ou PowerShell no Windows)

### Passo 1 — Baixe os arquivos do projeto
Coloque a pasta `sedra_gut` em qualquer local do seu computador.

### Passo 2 — Abra o terminal na pasta do projeto
```bash
cd caminho/para/sedra_gut
```

### Passo 3 — Instale as dependências (só na primeira vez)
```bash
pip install -r requirements.txt
```

### Passo 4 — Inicie o servidor
```bash
python app.py
```

### Passo 5 — Abra o navegador
Acesse: **http://localhost:5000**

---

## 👥 Uso em rede (vários usuários)

Para que outros computadores na mesma rede acessem o sistema:

1. Descubra o IP do computador que está rodando o servidor:
   - Windows: `ipconfig` no terminal → procure "Endereço IPv4"
   - Ex: `192.168.1.10`

2. Os outros usuários acessam pelo navegador:
   ```
   http://192.168.1.10:5000
   ```

3. O servidor deve estar rodando no computador "principal" enquanto os outros usam.

---

## 🗂️ Estrutura do projeto

```
sedra_gut/
├── app.py          ← Servidor principal (lógica das páginas)
├── database.py     ← Estrutura do banco de dados
├── requirements.txt← Dependências Python
├── instance/
│   └── sedra_gut.db← Banco de dados SQLite (criado automaticamente)
├── templates/
│   ├── login.html
│   ├── cadastro.html
│   └── dashboard.html
└── static/
    ├── style.css
    └── script.js
```

---

## 🔐 Segurança
- As senhas são **criptografadas** antes de salvar no banco (nunca salvas em texto puro)
- A sessão de login expira quando o navegador é fechado
- Para uso em produção (internet pública), consulte as instruções da V2

---

## 🗺️ Roadmap — Próximas versões

| Versão | Funcionalidades Planejadas |
|--------|---------------------------|
| V1.0626 | ✅ Matriz GUT, Login, Cadastro, Histórico de atividades |
| V2 | Integração Gmail, Drive e Google Agenda |
| V3 | Relatórios em PDF, gráficos de progresso |
| V4 | Notificações por e-mail automáticas |
| V5 | Dashboard executivo com indicadores |

---

## ❓ Problemas comuns

**"python não é reconhecido como comando"**
→ Instale o Python em python.org e marque "Add Python to PATH"

**"ModuleNotFoundError: No module named 'flask'"**
→ Rode novamente: `pip install -r requirements.txt`

**Página não abre no navegador**
→ Confirme que o terminal está mostrando "Running on http://..." e acesse o endereço exato

---

*SEDRA Consultoria — Sistema interno de gestão*
