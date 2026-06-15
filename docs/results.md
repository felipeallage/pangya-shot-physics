# Resultados

## Visão Geral

O projeto evoluiu de uma análise exploratória da Smart Calculator para uma implementação funcional de um simulador físico em Python, incluindo solver de potência, testes automatizados, análises exploratórias e dashboard interativo.

Ao final do desenvolvimento, o projeto conta com:

* 22 notebooks de análise e validação;
* 17 testes automatizados;
* Dashboard interativo em Streamlit;
* Simulação física completa de trajetória;
* Solver automático de potência;
* Conjunto de dados processados para análises comparativas;
* Documentação técnica do processo de engenharia reversa.

---

## Simulação Física

Foi implementado um modelo físico capaz de reproduzir trajetórias completas para diferentes tacos do PangYa.

Para cada simulação, o sistema calcula:

* distância final;
* altura máxima;
* tempo de voo;
* posição da bola em cada etapa da trajetória;
* influência do vento.

Exemplo de resultados obtidos:

| Taco | Distância Simulada (yd) |
| ---- | ----------------------: |
| 1W   |                  348.47 |
| 2W   |                  338.38 |
| 3W   |                  314.59 |
| 2I   |                  316.06 |
| 3I   |                  314.12 |
| 4I   |                  306.11 |
| 5I   |                  296.52 |
| 6I   |                  283.29 |
| 7I   |                  268.36 |
| 8I   |                  255.83 |
| 9I   |                  239.39 |
| PW   |                  222.88 |
| SW   |                  172.97 |

Os resultados apresentam comportamento consistente com a progressão esperada entre madeiras e ferros.

---

## Solver de Potência

Foi desenvolvido um solver capaz de determinar automaticamente a potência necessária para atingir uma distância alvo.

A solução utiliza busca binária, reduzindo significativamente o número de simulações necessárias para convergência.

Exemplos de cálculo:

| Distância Alvo | Potência Encontrada |
| -------------- | ------------------: |
| 50 yd          |              24.41% |
| 150 yd         |              44.75% |
| 200 yd         |              53.45% |
| 250 yd         |              61.72% |

O solver também retorna:

* erro final;
* número de iterações;
* distância atingida;
* status de convergência.

---

## Testes Automatizados

Foi criada uma suíte de testes utilizando Pytest para validar os principais componentes do sistema.

Cobertura atual:

* simulação de distância;
* comportamento dos tacos;
* modelo da bola;
* cálculo de vento;
* solver de potência.

Resultado atual:

```text
17 testes executados
17 testes aprovados
0 falhas
```

---

## Dashboard Interativo

Foi desenvolvido um dashboard em Streamlit para exploração dos resultados.

Funcionalidades:

* seleção de taco;
* configuração de distância alvo;
* configuração de vento;
* cálculo automático da potência;
* visualização gráfica da trajetória;
* exibição de métricas de voo.

O dashboard permite transformar os resultados da simulação em uma experiência visual e interativa.

---

## Visualizações e Análises

Foram desenvolvidas análises exploratórias para investigar:

* relação entre potência e distância;
* comportamento individual dos tacos;
* comparação de trajetórias;
* validação contra resultados da Smart Calculator;
* influência de parâmetros físicos no modelo.

Os resultados foram organizados em notebooks Jupyter e exportados para gráficos utilizados na documentação do projeto.

---

## Principais Aprendizados

Este projeto permitiu aplicar conceitos de:

* engenharia reversa;
* modelagem física;
* simulação numérica;
* algoritmos iterativos;
* testes automatizados;
* análise exploratória de dados;
* visualização de dados;
* desenvolvimento de dashboards.

Mais do que reproduzir resultados do jogo, o projeto serviu como estudo prático de modelagem matemática e construção de sistemas orientados a dados utilizando Python.

---

## Entregáveis Finais

* Código-fonte modular em Python;
* Pacote instalável (`src/pangya_physics`);
* Dashboard Streamlit;
* Testes automatizados;
* Notebooks de análise;
* Conjunto de dados processados;
* Documentação técnica;
* Estudos de validação e auditoria da Smart Calculator.

O resultado final é um projeto completo de engenharia reversa, simulação física e análise de dados, desenvolvido como estudo técnico e portfólio de Data Analytics e Python.
