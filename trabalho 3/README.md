  Passo 1:O programa lê as três listas que vieram do sistema do laboratório (nomes dos reagentes, códigos dos lotes e as purezas de cada frasco).
  Passo 2: Ele usa um `set` para limpar os nomes repetidos e mostrar na tela só os tipos de reagentes que a gente realmente tem no estoque.
  Passo 3: Com o comando `zip`, ele junta as três listas em uma coisa só, criando um "cadastro completo" para cada frasco.
  Passo 4: Usando *list comprehension* com um `if`, o script roda a lista inteira de uma vez e separa só os frascos que têm a pureza acima do que a gente precisa.
  Passo 5: No final, ele usa *unpacking* para abrir os dados de cada frasco selecionado e printa na tela um relatório limpo e o total de frascos encontrados.
