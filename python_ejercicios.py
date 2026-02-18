for i in range(5):
    print("hola")

for i in range(1, 6):
    print(i)

    nombres= ["ana","luis","andres"]

for nombre in nombres:
    print(nombre)

#ciclo while
contador=1

while contador <= 5:
    print(contador)
    contador += 1



respuesta = ""

while respuesta != "python":
    respuesta =input("Escribe 'python': ")

print("correcto")


#lambda

#x funcion normal

def sumar(a,b):
    return a+b


sumar = lambda a, b: a+b
print(sumar(3,4))


doble =  lambda x: x*2
print(doble(5))



es_par = lambda x: x % 2==0
print(es_par(4))
print(es_par(5))

#texto


texto =  "  hola mundo      "
limpio = texto.strip()
print(limpio)

#split

texto1 = "python es facil"
palabras = texto1.split()
print(palabras)

correo ="usuario@hotmail.com"
partes = correo.split("@")
print(partes)
#lower - minuscula
print("HOLA".lower())

#upper - mayuscula
print("hola".upper())

print("hola mundo".replace("mundo","python"))


texto2 = input("escribe una frase").strip()
palabras2 = texto2.split()

for palabra in palabras2:
    print(palabra)

numeros =[1,2,3,4,5,6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print (pares)


#sorted

personas = [
    {"nombre": "ana", "edad": 25},
    {"nombre": "pepito", "edad": 20}

]

ordenar = sorted(personas, key=lambda x: x["edad"])
print(ordenar)