import numpy
from colorama import Style, Fore, Back
import msvcrt
import os
import random

###################################
#Crear arreglo
libros = numpy.empty([10,4], object)




###################################
#Funciones de diseño
def printv(texto : str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr(texto : str):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")


def limpiarpantalla():
    printv("<<<<Presione una tecla para continuar>>>>")
    msvcrt.getch()
    os.system("cls")

###################################
#Funciones de arreglo

#Validar Codigo
def validarCodigo(cod):
    for i in range(10):
        if libros [i,0]==cod:
            return i
    return -1



#Guardar
def guardar(cod,autor,precio):
    if None in libros:
        if validarCodigo(cod)<0:
            if len(autor)>=4:
                if precio>=0:
                    for i in range(10):
                        if libros[i,0]==None:
                         libros[i,0]=cod
                         libros[i,1]=autor
                         libros[i,2]=precio
                         printv("Libro Registrado")
                         break
                else:
                    printr("El Precio debe ser mayor o Igual a 0")
            else:
                printr("El Autor debe tener minimo 4 caracteres")
        else:
            printr("Este Codigo ya esta registrado")
    else:
        printr("NO hay espacio disponible")



#Buscar
def buscarLibro():
    codigo=int(input("Ingrese Codigo para buscar el libro"))
    if codigo in libros:
        for i in range(10):
            if libros[i,0]==codigo:
                printv(f"Libro Encontrado.- Codigo: {libros[i,0]} .- Autor: {libros[i,1]} .- Precio: {libros[i,2]}")
                break
    else:
        printr("EL CODIGO NO ESTA REGISTRADO")






###################################
#Imprimir Certificado

criticas=[]
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")
criticas.append("Libro muy malo")


