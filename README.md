# Gerador de Senhas Aleatórias

Este é um simples gerador de senhas aleatórias em Python. Ele permite que você escolha a complexidade da senha e o seu tamanho.

## Requisitos

-   Python 3.x

## Uso

Primeiro, você precisa clonar este repositório para sua máquina local:

Copy code

`git clone https://github.com/seomarcos/gerador-de-senhas.git` 

Em seguida, navegue até a pasta do projeto e execute o script:

Copy code

`cd seu_repositorio
python3 gerador_senha.py` 

O programa irá solicitar que você insira a complexidade da senha (baixo, medio, alto) e o tamanho da senha que você deseja gerar. Depois disso, ele exibirá a senha gerada.

## Detalhes da Implementação

O script consiste em duas principais funções, `gerar_senha(complexidade, tamanho)` e `main()`.

A função `gerar_senha(complexidade, tamanho)` cria uma senha aleatória baseada na complexidade e no tamanho especificados. A complexidade determina os tipos de caracteres que podem ser incluídos na senha:

-   `baixo`: apenas letras (maiúsculas e minúsculas)
-   `medio`: letras e dígitos
-   `alto`: letras, dígitos e sinais de pontuação

Se uma complexidade inválida for fornecida, a função lançará um erro.

A função `main()` é a função de entrada do script. Ela solicita ao usuário a complexidade e o tamanho da senha, e então chama a função `gerar_senha()` para gerar e exibir a senha.

Por favor, note que este gerador de senhas é apenas para fins educacionais e pode não ser seguro para a geração de senhas em ambientes reais e de produção.
