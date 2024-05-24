
# Relatório de Pontuações de Alunos

Este projeto consiste em um sistema para processar um arquivo contendo informações sobre as pontuações de alunos e gerar um relatório com as somas das pontuações de cada aluno.

## Estrutura do Projeto

O projeto é dividido em vários componentes:

1. FileProcessor:

- Classe responsável por ler o arquivo de entrada.
- Verifica se o arquivo existe e se não está vazio.
- Gera um iterador para percorrer as linhas do arquivo.

2. LineProcessor:

- Classe responsável por processar cada linha do arquivo.
- Divide cada linha em palavras usando um delimitador especificado.

3. TextDialog:

- Classe responsável por exibir texto em uma janela GUI usando a biblioteca Tkinter.
- Fornece métodos para exibir texto normal e mensagens de erro.

4. Constants:

- Classe contendo constantes utilizadas em todo o projeto, como mensagens de erro e prompts de entrada.

5. Main

- Função principal que coordena o fluxo do programa.
- Solicita o nome do arquivo de entrada ao usuário.
- Processa cada linha do arquivo, calculando a soma das pontuações de cada aluno.
- Gera e exibe um relatório com as somas das pontuações.

## Estrutura Arquivo de Entrada 

O arquivo de entrada deve seguir o seguinte formato em cada linha:

 ```
    PrimeiroNome SegundoNome Nota
 ```

Onde:

- PrimeiroNome é o primeiro nome do aluno.
- UltimoNome é o último nome do aluno.
- Nota é a pontuação do aluno.

obs.: Cada informação é separada por espaço

## Como Funciona

Você fará anotações em um arquivo texto simples, colocando o nome, sobrenome e a nota do aluno, cada linha representando um aluno. Quando você fornece o nome do arquivo para o programa, ele lerá o arquivo, calculará a soma das pontuações de cada aluno e gerará um relatório com as somas das pontuações.
