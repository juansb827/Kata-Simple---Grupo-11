__author__ = ""

class Estadisticas:
    def calcular(self, cadenaInicial):
        if cadenaInicial == "": return 0
        elif len(cadenaInicial) == 1: return 1
        elif len(cadenaInicial.split(',')) == 2: return 2

