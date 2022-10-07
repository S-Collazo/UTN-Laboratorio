import re

'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("parcial\data.json")
    lista_exportable = lista_personajes
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Indicar opción:")
        if(respuesta=="1"):
            lista_altura = funciones.listar_por_altura(lista_personajes)
            lista_exportable = lista_altura
            print(lista_altura)
            
        elif(respuesta=="2"):
            funciones.altura_por_genero(lista_personajes)
            
        elif(respuesta=="3"):
            lista_peso = funciones.listar_por_peso(lista_personajes)
            lista_exportable = lista_peso
            print(lista_peso)
            
        elif(respuesta=="4"):
            while True:
                personaje_buscado = input("Indicar personaje a buscar:")
                verificador = re.search('[a-z0-9-]+', personaje_buscado, re.IGNORECASE)
                
                if not (verificador == None):
                    funciones.buscar_personaje(lista_personajes, personaje_buscado)
                    break
                
        elif(respuesta=="5"):
            funciones.exportar_csv(lista_exportable)
            
        elif(respuesta=="6"):
            break
        
        else:
            print("Opción incorrecta.")


starwars_app()

