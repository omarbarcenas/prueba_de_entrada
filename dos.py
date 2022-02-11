#from locale import str
#from builtins import int, list
from builtins import len
from pydantic import BaseModel
from dataclasses import dataclass

#@dataclass()
class videojuego(BaseModel):
    nombre: str
    horas: int
    genero: str
    plataforma: list

def suma_horas_de_juego(horas_uno: videojuego, horas_dos: videojuego) -> int:

    """Regresa la suma de las horas de juego
    
    Parametros: 
        horas_uno: primer objeto videojuego del cual se quieren sumar las horas de juego
        horas_dos: segundo objeto videojuego del cual se quieren sumar las horas de juego

    Regresa: El total de horas
        
        """
    return horas_uno.horas + horas_dos.horas

def suma_horas_de_lista_de_juegos(lista_juegos: list = [videojuego]) -> int:
    """Regresa la suma de horas de juego de una lista de juegos
    
    Parametros:
        lista_juegos: lista de videojuegos de los cuales se quieren sumar las horas de juego
    Regresa: El total de horas de la lista de juegos 
        """
    horas = 0
    for juego in range(len(lista_juegos)):
        horas = horas + lista_juegos[juego].horas

    return horas

if __name__=="__main__":
    gow = videojuego(nombre = "god of war", horas= 30, genero="Hack", plataforma= ["playstation", "pc"])
    zel = videojuego(nombre = "zelda", horas = 15, genero = "adventure", plataforma=["wiiu"])
    age = videojuego(nombre = "age of empires", horas = 180, genero = "estrategia", plataforma=["pc"])
    inj = videojuego(nombre = "injustice", horas = 150, genero = "peleas", plataforma=["playstation", "xbox", "pc"])

    horas_totales = suma_horas_de_juego(gow, zel)
    print(f"las horas totales de los dos juegos son {horas_totales}")

    horas_totales_lista = suma_horas_de_lista_de_juegos([age, inj])
    print(f"las horas totales de la lista de juegos son {horas_totales_lista}")