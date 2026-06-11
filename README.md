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
* Solver de potência implementado
* Auditoria inicial dos tacos concluída
* Notebooks de validação e análise
* Versionamento ativo via GitHub

---

## Estrutura do Projeto

```text
pangya-shot-physics/
│
├── notebooks/
├── docs/
├── src/
│   └── pangya_physics/
├── tests/
├── data/
└── app/
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
* [ ] Dataset Analítico
* [ ] Comparação Python vs Smart Calc

### Fase 5 — Analytics e Visualização

* [ ] Dashboard Streamlit
* [ ] Visualização 3D
* [ ] Gráficos interativos
* [ ] Deploy

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
