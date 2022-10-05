import json
import re

def cargar_json(data:str) -> list:
    """
    Recibe la dirección de un archivo json.
    Carga su contenido a una lista.
    Retorna esa lista.
    """
    
    dict_json = {}
    lista_json = []
    
    with open(data, 'r') as archivo:
        dict_json = json.load(archivo)
        lista_json.append(dict_json)
        
    lista_personajes = lista_json[0]["results"]
    
    return lista_personajes

def exportar_csv(lista_a_exportar:list):
    """
    Recibe una lista a exportar.
    Convierte cada entrada de la misma en una línea de string con todos sus datos.
    Escribe esa línea en un archivo CSV (en caso de ya existir, lo sobreescribe).
    No retorna nada.
    """

    lista_exportable = lista_a_exportar[:]
    
    with open("parcial\data_ordenada.csv", 'w+') as archivo:
        for personaje in lista_exportable:
            texto = "Nombre: {0} | Altura: {1} | Peso: {2} | Genero: {3} \n"
            texto = texto.format(personaje["name"], personaje["height"], personaje["mass"], personaje["gender"])
            archivo.write(texto)
  
def listar_por_altura(lista_personajes:list) -> list:
    """
    Recibe una lista de personajes.
    Recorre la lista y ordena de acuerdo a la altura.
    Retorna la lista ordenada.
    """
    
    lista_pers = lista_personajes[:]
    lista_iz = []
    lista_de = []

    if(len(lista_pers) <= 1):
        lista_altura = lista_pers
    else:
        pivot = lista_pers[0]
        valor_pivot = int(pivot["height"])
        
        for i in range(1,len(lista_pers)):
            personaje = lista_pers[i]
            valor_altura_pers = int(personaje["height"])
            
            if valor_altura_pers < valor_pivot:
                lista_iz.append(personaje)
            else:
                lista_de.append(personaje)
        
        lista_iz.append(pivot)
        lista_iz = listar_por_altura(lista_iz)
        lista_de = listar_por_altura(lista_de)
        
        lista_altura = lista_iz + lista_de
        
    return lista_altura
        
def altura_por_genero(lista_altura:list):
    """
    Recibe una lista de personajes.
    Recorre la lista, la ordena por altura y guarda en variables los personajes más altos de cada género.
    Informa el nombre y altura de esos personajes.
    No retorna nada.
    """
    
    lista_alt = lista_altura[:]
    lista_alt_m = []
    lista_alt_f = []
    lista_alt_n = []
    
    for personaje in lista_alt:
        valor_genero = personaje["gender"]
        
        if(valor_genero == "male"):
            lista_alt_m.append(personaje)
        elif(valor_genero == "female"):
            lista_alt_f.append(personaje)
        else:
            lista_alt_n.append(personaje)
           
    lista_alt_m = listar_por_altura(lista_alt_m)
    lista_alt_f = listar_por_altura(lista_alt_f)
    lista_alt_n = listar_por_altura(lista_alt_n)
    
    mas_alto_m = lista_alt_m[-1]
    mas_alto_f = lista_alt_f[-1]
    mas_alto_n = lista_alt_n[-1]
    
    mensaje = "Personaje masculino más alto: {0}, {1}cm. \n".format(mas_alto_m["name"], mas_alto_m["height"])
    mensaje += "Personaje femenino más alto: {0}, {1}cm. \n".format(mas_alto_f["name"], mas_alto_f["height"])
    mensaje += "Personaje no-definido más alto: {0}, {1}cm.".format(mas_alto_n["name"], mas_alto_n["height"])
    
    print(mensaje)
    
def listar_por_peso(lista_personajes:list) -> list:
    """
    Recibe una lista de personajes.
    Recorre la lista y ordena de acuerdo al peso.
    Retorna la lista ordenada.
    """
    
    lista_pers = lista_personajes[:]
    lista_iz = []
    lista_de = []

    if(len(lista_pers) <= 1):
        lista_peso = lista_pers
    else:
        pivot = lista_pers[0]
        valor_pivot = int(pivot["mass"])
        
        for i in range(1,len(lista_pers)):
            personaje = lista_pers[i]
            valor_peso_pers = int(personaje["mass"])
            
            if valor_peso_pers < valor_pivot:
                lista_iz.append(personaje)
            else:
                lista_de.append(personaje)
        
        lista_iz.append(pivot)
        lista_iz = listar_por_peso(lista_iz)
        lista_de = listar_por_peso(lista_de)
        
        lista_peso = lista_iz + lista_de

    return lista_peso
    
def buscar_personaje(lista_personaje:list, personaje_buscado:str):
    """
    Recibe una lista de personajes y un string con el nombre (o parte del nombre) del personaje a buscar.
    Busca en la lista coincidencias con el string indicado.
    Si hay coincidencias, imprime los personajes que coinciden. Si no, informa que no se encontrò ninguno.
    No retorna nada.
    """
    
    lista_pers = lista_personaje[:]
    verificador = False
    
    for personaje in lista_pers:
        buscador = re.search(personaje_buscado, personaje["name"], re.IGNORECASE)
        if not (buscador == None):
            print(personaje)
            verificador = True
            
    if(verificador == False):
        print("No se encontró el personaje.")


test = cargar_json("parcial\data.json")
test_2 = print(listar_por_peso(test))