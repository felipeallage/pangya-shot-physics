# Auditoria dos Tacos (Club Audit)

## Objetivo

Avaliar o comportamento dos tacos implementados no simulador físico e verificar se os parâmetros cadastrados reproduzem uma hierarquia de distância, altura e tempo de voo coerente com o esperado no PangYa.

---

## Metodologia

Foi executada uma simulação para cada taco utilizando:

* Vento = 0
* Potência = 100%
* Mesma física para todos os testes
* Registro de:

  * Distância final
  * Altura máxima
  * Tempo de voo

Os resultados foram comparados entre Woods, Irons e Wedges.

---

## Primeira Descoberta

Inicialmente a função `create_initial_velocity()` utilizava:

```python
initial_power = club.power_base * power_percent
```

Os resultados apresentaram inconsistências relevantes:

* 2W superando 1W em distância.
* PW e SW produzindo distâncias negativas.
* Hierarquia incoerente entre tacos.

Esses resultados indicaram que o parâmetro utilizado para gerar a velocidade inicial não representava corretamente o comportamento esperado.

---

## Investigação

Durante a auditoria foi observado que o modelo de dados dos tacos possui dois parâmetros relacionados à potência:

```python
power_base
power_factor
```

Foi realizado um experimento substituindo:

```python
power_base
```

por:

```python
power_factor
```

na função de cálculo da velocidade inicial.

---

## Resultado

Após a alteração, a hierarquia dos tacos passou a apresentar comportamento significativamente mais coerente.

### Ranking de Distância

| Taco | Distância |
| ---- | --------: |
| 1W   |    348.47 |
| 2W   |    338.38 |
| 2I   |    316.06 |
| 3W   |    314.59 |
| 3I   |    314.12 |
| 4I   |    306.11 |
| 5I   |    296.52 |
| 6I   |    283.29 |
| 7I   |    268.36 |
| 8I   |    255.83 |
| 9I   |    239.39 |
| PW   |    222.88 |
| SW   |    172.97 |

---

## Análise de Altura

As alturas máximas apresentaram um comportamento consistente com o esperado:

### Woods

Trajetórias mais baixas:

* 1W → 18.51
* 2W → 23.45
* 3W → 26.75

### Irons

Trajetórias intermediárias:

* 2I → 34.35
* 5I → 54.88
* 9I → 77.32

### Wedges

Trajetórias mais altas:

* PW → 82.50
* SW → 71.84

---

## Conclusões

### Confirmado

A utilização de `power_factor` produz resultados mais coerentes que `power_base` para o cálculo da velocidade inicial.

### Evidências

* Hierarquia de distância mais próxima do esperado.
* Trajetórias progressivamente mais altas conforme o loft aumenta.
* Eliminação das distâncias negativas observadas anteriormente.

### Limitações

Ainda existem pequenas inconsistências entre alguns tacos (por exemplo 2I, 3W e 3I apresentando alcances muito próximos).

Essas diferenças provavelmente estão relacionadas à simplificação atual do modelo físico, que ainda não incorpora completamente elementos presentes na Smart Calc original, como:

* Power Shot
* Spin
* Curve
* Tomahawk
* Cobra
* Spike
* Ajustes específicos por taco

---

## Status

✅ Auditoria concluída

✅ Problema identificado

✅ Correção aplicada

✅ Resultados documentados

Próxima etapa: visualização e comparação gráfica das trajetórias dos tacos.
