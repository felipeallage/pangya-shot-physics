# Como Executar

## Clonar o Repositório

```bash
git clone https://github.com/felipeallage/pangya-shot-physics.git

cd pangya-shot-physics
```

## Criar Ambiente Virtual

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## Instalar Dependências

```bash
pip install -r requirements.txt
```

## Executar Testes

```bash
pytest
```

---

## Executar Dashboard

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador.

---

## Executar Notebooks

```bash
jupyter notebook
```

ou

```bash
jupyter lab
```

---

## Estrutura Principal

```text
src/
tests/
notebooks/
data/
docs/
app.py
```

---

## Requisitos

* Python 3.11+
* Git
* Streamlit
* Jupyter Notebook
