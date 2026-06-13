# PangYa Shot Physics

Projeto de engenharia reversa, simulação física e análise de dados baseado na Smart Calculator de Acrisio para PangYa.

---

## Objetivo

O objetivo deste projeto não é simplesmente reproduzir a Smart Calculator original.

A proposta é:

* compreender e documentar o modelo físico do PangYa;
* reimplementar gradualmente o simulador em Python;
* validar resultados contra a Smart Calc original;
* criar análises de sensibilidade;
* desenvolver visualizações interativas;
* construir um portfólio de Analytics e Simulação.

---

## Motivação

PangYa foi um dos principais responsáveis pelo meu interesse em Excel, modelagem matemática e análise de sistemas.

Durante muitos anos a comunidade criou tabelas, planilhas e modelos empíricos para prever tacadas.

Posteriormente, Acrisio realizou engenharia reversa do jogo e desenvolveu a Smart Calculator, permitindo simulações muito mais próximas do comportamento real do PangYa.

Este projeto busca transformar esse conhecimento em um estudo moderno de:

* Python
* Simulação Física
* Data Analytics
* Visualização de Dados
* Engenharia Reversa

---

## Tecnologias

### Atualmente

* Python
* NumPy
* Pandas
* Matplotlib
* Jupyter Notebook
* Pytest
* Git
* GitHub

### Futuras

* Plotly
* Streamlit
* Docker

---

## Status Atual

Atualmente o projeto conta com:

* Estrutura completa como pacote Python
* 17 testes automatizados passando
* Simulador físico funcional
* Solver de potência implementado e validado
* Dashboard interativo em Streamlit
* Dataset analítico completo dos tacos
* Auditoria quantitativa do solver
* Visualizações de trajetória
* Comparação entre tacos
* Exportação de datasets CSV
* Versionamento ativo via GitHub
---

## Estrutura do Projeto

```text
pangya-shot-physics/

├── app.py
│
├── notebooks/
│   ├── 01_smart_calc_audit.ipynb
│   ├── 02_club_analysis.ipynb
│   ├── 03_find_power_validation.ipynb
│   ├── 04_club_dataset_analysis.ipynb
│   ├── 05_club_visualizations.ipynb
│   └── 06_trajectory_visualizations.ipynb
│
├── src/
│   └── pangya_physics/
│
├── tests/
│
├── docs/
│   └── images/
│
├── data/
│   └── processed/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```
---

## Componentes Implementados

### Vector3D

Responsável por:

* soma vetorial
* subtração
* normalização
* produto vetorial
* magnitude

---

### Ball

Representa o estado físico da bola.

Inclui:

* posição
* velocidade
* spin
* curva
* rotações
* massa
* altura máxima

---

### Club

Modela os tacos do PangYa.

Atualmente:

* Woods
* Irons
* Wedges

Propriedades:

* power_factor
* power_base
* loft (degree)
* rotation_spin
* rotation_curve

---

### Wind

Conversão de:

* intensidade
* direção

para vetores tridimensionais.

---

### Simulator

Motor físico responsável pela simulação da trajetória da bola.

Atualmente implementa:

* gravidade
* vento
* curva
* spin
* resistência do ar (drag)

---

### Solver

Implementação de busca binária para cálculo da potência necessária para atingir uma distância-alvo.

Atualmente inclui:

* `find_velocity_for_distance()`
* `find_height_collision()`
* `find_power()`

O solver foi validado através de múltiplos testes e análises, apresentando convergência consistente para diferentes tacos e distâncias.

Também é capaz de identificar automaticamente cenários fisicamente impossíveis.

---

## Análises Desenvolvidas

### Club Analysis

Análise dos parâmetros dos tacos:

* Power Factor
* Power Base
* Rotation Spin
* Rotation Curve
* Loft

Notebook:

```text
02_club_analysis.ipynb
```

---

### Basic Trajectory

Primeiras simulações de trajetória.

Notebook:

```text
03_basic_trajectory.ipynb
```

---

### Sensitivity Analysis

Comparação de cenários:

* sem vento
* vento frontal
* vento traseiro
* vento lateral
* spin
* curva

Notebook:

```text
04_sensitivity_analysis.ipynb
```

---

### Distance Solver

Busca de velocidade para distância-alvo.

Notebook:

```text
05_distance_solver.ipynb
```

---

### Solver Grid Analysis

Avaliação do solver para múltiplas distâncias.

Notebook:

```text
06_solver_grid_analysis.ipynb
```

---

### Club Solver Comparison

Comparação entre tacos.

Notebook:

```text
07_club_solver_comparison.ipynb
```

---
## Validação do Solver

O algoritmo `find_power()` foi submetido a testes utilizando múltiplos tacos e diferentes distâncias alvo.

Resultados observados:

* Convergência em todos os cenários válidos analisados
* Erro absoluto máximo inferior a 0.5 jarda
* Média de convergência entre 7 e 8 iterações
* Resultados consistentes entre Woods, Irons e Wedges

Esses resultados indicam que a implementação atual é estável para utilização em análises e simulações.

---

### Power Audit

Validação do algoritmo `find_power()` para diferentes tacos e distâncias.

Objetivos:

* medir convergência;
* avaliar erro residual;
* identificar distâncias inalcançáveis;
* validar comportamento físico do simulador.

Notebook:

```text
17_power_audit.ipynb
```

---

```markdown
## Dashboard Streamlit

O projeto possui um dashboard interativo desenvolvido em Streamlit.

Funcionalidades:

* Seleção de taco
* Distância alvo
* Configuração de vento
* Cálculo automático da potência necessária
* Visualização da trajetória da bola
* Métricas de voo
    * potência necessária
    * distância final
    * erro
    * altura máxima
    * tempo de voo
```

## Resultados Preliminares

Alguns insights já observados:

* Relação não linear entre potência e distância.
* Diferenças significativas de trajetória entre Woods, Irons e Wedges.
* O solver converge de forma consistente para múltiplos cenários.
* O simulador consegue identificar automaticamente limitações físicas dos tacos.
* Exemplo observado durante os testes: um SW não consegue atingir 300y mesmo em potência máxima.

O foco das próximas etapas será transformar essas simulações em datasets analíticos e visualizações exploratórias.

---

## Roadmap

### Fase 1 — Estrutura e Física Básica

* [x] Estrutura do projeto
* [x] Vetores 3D
* [x] Ball
* [x] Club
* [x] Wind
* [x] Simulator básico
* [x] Testes unitários

### Fase 2 — Simulação e Validação

* [x] Solver inicial
* [x] Club Analysis
* [x] Trajetórias básicas
* [x] Sensitivity Analysis

### Fase 3 — Engenharia Reversa da Smart Calc

* [ ] Portar `initShot()`
* [ ] Portar `getSlope()`
* [ ] Portar `getValuesDegree()`

### Fase 4 — Solver Avançado e Auditoria

* [x] Implementar `find_power()`
* [x] Power Audit
* [x] Dataset Analítico
* [ ] Comparação Python vs Smart Calc

### Fase 5 — Analytics e Visualização

* [x] Dashboard Streamlit
* [x] Visualizações de Trajetória
* [x] Curvas de Potência
* [x] Exportação de Datasets
* [ ] Visualização 3D
* [ ] Deploy

---

## Principais Resultados

Até o momento o projeto já produziu:

* Simulador físico funcional
* Solver de potência validado
* Dataset analítico dos tacos
* Curvas de potência
* Comparações de trajetória
* Dashboard interativo
* Testes automatizados
* Documentação técnica

O projeto evoluiu de uma simples reimplementação da Smart Calculator para uma plataforma de estudo de física, simulação e análise de dados aplicada ao PangYa.

---

## Diferencial do Projeto

A Smart Calculator original é uma ferramenta para uso no jogo.

Este projeto possui outro foco:

| Smart Calc       | PangYa Shot Physics      |
| ---------------- | ------------------------ |
| Calculadora      | Projeto Analítico        |
| JavaScript       | Python                   |
| Foco em jogar    | Foco em entender         |
| Resultado direto | Documentação e validação |
| Ferramenta       | Portfólio de Dados       |

O objetivo não é apenas reproduzir resultados, mas compreender, documentar e analisar o comportamento físico do jogo através de métodos modernos de simulação e análise de dados.

---

## Autor

Felipe Augusto Allage

Projeto desenvolvido para aprofundamento em:

* Python
* Simulação Física
* Data Analytics
* Engenharia Reversa
* Visualização de Dados
* Desenvolvimento de Portfólio Técnico


- Python
- Simulação
- Data Analytics
- Engenharia Reversa
- Visualização de Dados
