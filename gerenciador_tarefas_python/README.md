# Gerenciador de Tarefas em Python

Um projeto simples de linha de comando para praticar fundamentos de Python, organização de código e testes automatizados.

## Funcionalidades

- Listar tarefas
- Adicionar tarefas
- Concluir tarefas
- Remover tarefas
- Testes automatizados com `unittest`

## Requisitos

- Python 3.10 ou superior

## Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/gerenciador-tarefas.git
cd gerenciador-tarefas
```

Execute:

```bash
python main.py
```

No Linux/macOS, também pode ser necessário usar:

```bash
python3 main.py
```

## Como executar os testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
gerenciador-tarefas/
├── main.py
├── src/
│   ├── __init__.py
│   └── task_manager.py
├── tests/
│   └── test_task_manager.py
├── .gitignore
├── LICENSE
└── README.md
```
## Licença

MIT.
