import string
import random

def gerar_senha(complexidade, tamanho):
    caracteres = {
        'baixo': string.ascii_letters,
        'medio': string.ascii_letters + string.digits,
        'alto': string.ascii_letters + string.digits + string.punctuation
    }
    
    if complexidade not in caracteres:
        raise ValueError("Complexidade inválida. Escolha entre 'baixo', 'medio' ou 'alto'.")
        
    return ''.join(random.choices(caracteres[complexidade], k=tamanho))

def main():
    print("Gerador de Senhas Aleatórias")
    
    complexidade = input("Digite a complexidade (baixo, medio, alto): ")
    tamanho = int(input("Digite o tamanho da senha: "))
    
    senha = gerar_senha(complexidade, tamanho)
    print(f"A senha gerada é: {senha}")

if __name__ == '__main__':
    main()
