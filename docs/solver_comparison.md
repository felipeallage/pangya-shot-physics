## Análise de Desempenho dos Solvers

Duas estratégias diferentes de solver foram implementadas e comparadas durante o desenvolvimento do projeto.

### Solver por Busca Binária (Binary Search)

Um algoritmo determinístico que reduz progressivamente o intervalo de busca até encontrar a potência necessária para atingir a distância desejada.

#### Vantagens

* Convergência rápida
* Comportamento estável
* Tempo de execução previsível
* Adequado como solver principal do projeto

#### Desvantagens

* Menos parecido com a lógica original da Smart Calc
* Menor valor para fins de engenharia reversa

---

### Solver por Feed Adaptativo (Smart Style Feed)

Uma abordagem iterativa inspirada no comportamento da Smart Calc original, ajustando a potência gradualmente até atingir o alvo.

#### Vantagens

* Mais próximo da lógica utilizada pela Smart Calc
* Útil para estudos de engenharia reversa
* Permite compreender melhor o comportamento do algoritmo original

#### Desvantagens

* Quantidade significativamente maior de iterações
* Sensível à calibração do parâmetro de ajuste (feed)
* Pode exigir muitas iterações para convergir

---

## Resultados Experimentais

Resultados médios obtidos durante os testes de validação:

| Métrica             | Busca Binária | Smart Style Feed |
| ------------------- | ------------- | ---------------- |
| Média de Iterações  | 36            | 520              |
| Erro Absoluto Médio | 0,35          | 0,36             |

---

## Conclusão

Os dois métodos apresentaram níveis de precisão muito semelhantes.

Entretanto, o método de Busca Binária encontrou a solução aproximadamente **14 vezes mais rápido**, tornando-se a implementação preferencial para o estado atual do projeto.

O solver Smart Style Feed permanece como uma importante referência de pesquisa e engenharia reversa, permitindo compreender melhor o funcionamento da Smart Calc original e servindo como base para futuras investigações e refinamentos do modelo.

### Observação

O objetivo deste projeto não é apenas reproduzir os resultados da Smart Calc, mas também compreender, validar e documentar o comportamento do modelo físico por trás da calculadora. Por esse motivo, diferentes abordagens de solver foram implementadas, comparadas e auditadas ao longo do desenvolvimento.
