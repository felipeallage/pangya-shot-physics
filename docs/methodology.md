# Metodologia

## Objetivo

Este projeto tem como objetivo estudar, documentar e reimplementar parte do modelo físico utilizado pela Smart Calculator de PangYa utilizando Python.

O foco não é reproduzir exatamente o código original, mas compreender os mecanismos físicos envolvidos no cálculo de trajetórias e potência.

---

## Processo de desenvolvimento

O projeto foi dividido em quatro etapas principais:

### 1. Auditoria da Smart Calculator

Inicialmente foram realizados experimentos controlados na Smart Calculator original para compreender:

* comportamento da trajetória;
* influência do vento;
* influência dos tacos;
* relação entre potência e distância;
* comportamento do solver de potência.

Os resultados foram registrados em notebooks exploratórios.

---

### 2. Modelagem Física

Após a auditoria, foi criada uma implementação própria utilizando Python.

Os principais componentes modelados foram:

* Bola
* Taco
* Vento
* Vetores tridimensionais
* Simulador de trajetória

A trajetória é calculada passo a passo utilizando integração numérica.

---

### 3. Solver de Potência

Foi implementado um solver capaz de encontrar automaticamente a potência necessária para atingir uma determinada distância.

O algoritmo utiliza busca binária para reduzir o número de simulações necessárias.

---

### 4. Validação

Os resultados produzidos pelo simulador foram comparados com valores obtidos pela Smart Calculator.

Foram analisados:

* distância final;
* altura máxima;
* tempo de voo;
* comportamento sob vento;
* comportamento por taco.

---

## Ferramentas utilizadas

* Python
* NumPy
* Pandas
* Matplotlib
* Plotly
* Streamlit
* Pytest
* Jupyter Notebook

---

## Estrutura do Projeto

* Simulação física
* Solver de potência
* Testes automatizados
* Análises exploratórias
* Dashboard interativo
