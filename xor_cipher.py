import random
cadena = "creado por Josue" 

key = [random.choice([0,1]) for _ in cadena]

def encripDesencrip(Input, xorKey):

    resultado = ""
    
    for i in range(len(Input)):
        resultado += chr(ord(Input[i]) ^ xorKey[i])

    return resultado

cifrado = encripDesencrip(cadena, key)
descifrado = encripDesencrip(cifrado, key)

print(f"Original: {cadena}")
print(f"Clave: {key}") 
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {descifrado}")
