#1
nombre = "Sofia"
edad = 27
comidaFavorita = "Tacos"
presentacion = f"Hola! Mi nombre es {nombre}. Yo tengo {edad} años, y mi comida favorita es el {comidaFavorita}"
print(presentacion)

#2
fullName = input("Ingrese su nombre completo: ")
nombresinEspacios = fullName.replace(" ", "")
cantidadLetras = len(nombresinEspacios)
print(f"¡Hola, {fullName}! Tu nombre tiene {cantidadLetras} letras, excluyendo los espacios.")

#3
ventas = float(input("Ingrese el porcentaje de aumento de ventas: "))
ingresos = float(input("Ingrese el porcentaje de crecimiento de ingresos: "))

resultado = f"Las ventas aumentaron un {ventas:.2f}% y los ingresos crecieron un {ingresos:.2f}%."
print(resultado)


#4
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
mensajeDecodificado = secretMessage[3::2]
print(mensajeDecodificado)

#5
def contar_frases(texto):
    frases = texto.split('.')
    return len([frase for frase in frases if frase.strip()])

texto = "El carro que me regalo mi papa me gusta mucho"
numero_frases = contar_frases(texto)
print(f"Número de frases en el texto: {numero_frases}")

#6
def cambiarVocal(cadena, vocalAntigua, vocalNueva):
    return cadena.replace(vocalAntigua, vocalNueva)

frase = "que dice mi gente"
nuevaFrase = cambiarVocal(frase, "e", "i")
print(nuevaFrase)




