#Problema 1
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = list(set(lista_original))
print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)

#Problema 2
nombre_archivo = input("PC2").strip().lower()
tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

tipo = "application/octet-stream"

for extension, mime in tipos_mime.items():
    if nombre_archivo.endswith(extension):
        tipo = mime
        break

print("Tipo MIME:", tipo)

#Problema 3
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        print(numero)

#Problema 4
for i in range(1, 6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)

#Problema 5
numeros = []

while True:
    desea = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    if desea == "NO":
        break
    if desea == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números ingresados:", numeros)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)

#Problema 6
alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o escriba FIN para terminar): ")
    if nombre.upper() == "FIN":
        break
    
    notas = []
    for i in range(3):
        nota = int(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    
    alumno = {"Alumno": nombre, "Notas": notas}
    alumnos.append(alumno)

print("\nListado de alumnos:")
for alumno in alumnos:
    print(alumno)

#Problema 7
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

suma_primos = 0

for n in range(100):
    if es_primo(n):
        suma_primos += n

print("La suma de primos menores que 100 es:", suma_primos)

#Problema 8
a, b = 0, 1

while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

#Problema 9
def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

for n in range(1, 1000):
    if es_numero_perfecto(n):
        print("Número perfecto:", n)

#Problema 10
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número: "))
print("El factorial es:", factorial(numero))

#Problema 11
texto = input("Ingrese un texto: ")

vocales = "aeiouAEIOU"
resultado = ""

for letra in texto:
    if letra not in vocales:
        resultado += letra

print("Texto sin vocales:", resultado)

#Problema 12
meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

fecha = input("Ingrese una fecha (ejemplo: 9/8/1636 o Septiembre 8, 1636): ").strip()

if "/" in fecha:
    mes, dia, anio = fecha.split("/")
    mes = int(mes)
    dia = int(dia)
    anio = int(anio)
else:
    mes_palabra, resto = fecha.split(" ", 1)
    dia, anio = resto.replace(",", "").split()
    mes = meses.index(mes_palabra) + 1
    dia = int(dia)
    anio = int(anio)

print(f"{anio}-{mes:02}-{dia:02}")
