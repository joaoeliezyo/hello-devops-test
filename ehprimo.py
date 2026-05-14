def eh_primo(num):
    "Verifica se um número é primo."
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def enesimo_primo(n):
    "Encontra o n-ésimo número primo."
    contador = 0
    numero_atual = 1
    
    while contador < n:
        numero_atual += 1
        if eh_primo(numero_atual):
            contador += 1
            
    return numero_atual


# n = int(input("Digite o valor de n: "))
resultado = enesimo_primo(n)
print(f"O {n}º número primo é: {resultado}")