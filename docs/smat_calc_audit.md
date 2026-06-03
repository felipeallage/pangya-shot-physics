# Smart Calc Audit

## 1. Objetivo do documento

Este documento registra a auditoria técnica inicial da Smart Calculator do PangYa, criada por Acrisio.

O objetivo não é apenas traduzir o código JavaScript para Python, mas entender a estrutura do modelo físico, separar responsabilidades e criar uma base documentada para:

- reimplementação em Python;
- validação contra a Smart Calc original;
- análise de sensibilidade;
- visualização das trajetórias;
- construção futura de dashboard.

---

## 2. Fonte original

Arquivo analisado:

```text
smart_calculator.js