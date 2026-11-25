# Algoritmos de Ordenação

Este trabalho compara três algoritmos de ordenação: Gnome Sort, Tournament Sort e Pancake Sort.

## Gnome Sort

O Gnome Sort percorre a lista comparando elementos adjacentes. Quando estão na ordem incorreta, eles são trocados. Caso contrário, o algoritmo avança para o próximo elemento. Esse processo continua até que toda a lista esteja ordenada.

## Tournament Sort

O Tournament Sort utiliza a estrutura de um torneio para identificar repetidamente o menor elemento entre os valores disponíveis. O elemento selecionado é colocado na posição correspondente do resultado ordenado, e o processo continua até que todos os elementos sejam organizados.

## Pancake Sort

O Pancake Sort ordena os elementos utilizando operações de inversão de partes da lista. Em cada etapa, identifica o maior elemento da parte ainda não ordenada e utiliza inversões para colocá-lo na posição correta.

## Finalidade da comparação

Os três algoritmos serão avaliados utilizando conjuntos de dados de nomes com 100.000, 250.000 e 500.000 elementos. O principal critério de comparação será o tempo de execução.