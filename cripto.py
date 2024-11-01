frase = str(input("Digite sua palavra: "))

def letra_para_numero(palavra, separador='-'):
    resultado = []
    for letra in palavra:
        if letra.isalpha():  # Verifica se é uma letra
            numero = ord(letra.lower()) - ord('a') + 1  # Calcula a posição
            resultado.append(str(numero))
    return separador.join(resultado)


palavra = frase
resultado = letra_para_numero(palavra)
print("Sua palavra criptografada é: {}".format(resultado))  # Saída
