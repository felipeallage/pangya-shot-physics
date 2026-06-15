# Limitações

Este projeto é uma reimplementação independente inspirada na Smart Calculator.

O objetivo é compreender e reproduzir o comportamento geral do sistema, e não criar uma cópia exata do jogo.

---

## Calibração dos Tacos

Alguns tacos ainda apresentam diferenças em relação ao comportamento esperado no jogo.

Exemplo:

* o 2I apresenta distância ligeiramente superior ao 3W em determinados cenários;

Esse resultado sugere que ainda existem parâmetros físicos que podem ser refinados.

---

## Modelo Aerodinâmico

O modelo atual utiliza simplificações para:

* resistência do ar;
* sustentação;
* interação com vento.

A implementação não pretende reproduzir todos os detalhes internos do PangYa.

---

## Solver

O solver utiliza busca binária.

Dependendo da tolerância configurada, alguns resultados podem ser classificados como "não encontrados" mesmo quando o erro final é pequeno.

---

## Escopo

O projeto não contempla:

* spin;
* curva;
* terreno inclinado;
* efeitos especiais;
* condições específicas de determinados personagens ou equipamentos.

---

## Trabalho Futuro

* calibração fina dos tacos;
* validação contra mais cenários da Smart Calculator;
* suporte a spin e curva;
* análises estatísticas adicionais;
* expansão do dashboard.
