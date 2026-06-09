# Auditoria do Solver: Sensibilidade à Altura

## Objetivo

Avaliar como a primeira versão do `find_power` responde a diferentes alturas de alvo mantendo a distância fixa em 200 jardas.

## Configuração

- Taco: 1W
- Distância alvo: 200
- Vento: 0
- Alturas testadas: -20, -10, 0, 10, 20, 30, 40

## Resultado observado

Alturas negativas apresentaram comportamento coerente:

- Altura -20 exigiu menos power que altura 0.
- Altura -10 exigiu menos power que altura 0.
- Altura 0 serviu como referência.

Alturas positivas saturaram no limite máximo de power:

- +10 → 130%
- +20 → 130%
- +30 → 130%
- +40 → 130%

## Diagnóstico

A versão atual do solver modela o ponto em que a trajetória cruza uma determinada altura durante o voo.

Isso é diferente do problema completo da Smart Calc, que busca calcular a força necessária para atingir um alvo definido por distância e altura.

## Conclusão

O comportamento encontrado não deve ser tratado como simples erro numérico. Ele revela uma limitação conceitual da primeira versão do solver.

A próxima etapa será comparar esse comportamento com a implementação original da Smart Calc, especialmente as funções relacionadas a:

- `altura_colision`
- `find_power`
- ajuste iterativo de `percentShot`
- cálculo de desvio
- tratamento de altura no alvo

## Status

Limitação identificada e documentada.