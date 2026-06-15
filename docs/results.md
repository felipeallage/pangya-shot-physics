# Resultados

## Simulação Física

Foi possível reproduzir trajetórias completas para diferentes tacos utilizando um modelo físico próprio.

O simulador calcula:

* distância final;
* altura máxima;
* tempo de voo;
* trajetória completa da bola.

---

## Solver de Potência

O solver desenvolvido encontra a potência necessária para atingir uma distância alvo utilizando busca binária.

Exemplo:

| Distância |
| --------- |
| 50 yd     |
| 100 yd    |
| 150 yd    |
| 200 yd    |
| 250 yd    |

O número médio de iterações foi significativamente menor que o método de busca incremental utilizado como referência.

---

## Comparação entre Tacos

Foram geradas análises comparando:

* distância máxima;
* altura máxima;
* tempo de voo.

Os resultados mostraram comportamento consistente entre madeiras e ferros.

---

## Dashboard

Foi desenvolvido um dashboard em Streamlit que permite:

* selecionar o taco;
* definir distância alvo;
* configurar vento;
* visualizar a trajetória;
* calcular potência automaticamente.

---

## Principais Aprendizados

* Engenharia reversa de sistemas físicos.
* Simulação numérica em Python.
* Construção de solvers iterativos.
* Testes automatizados.
* Visualização de dados.
* Comunicação de resultados técnicos.
