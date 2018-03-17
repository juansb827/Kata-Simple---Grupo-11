__author__ = ""


class Estadisticas:
    def calcular(self, cadenaInicial):
        if cadenaInicial == "":
            return 0
        else:
            return len(cadenaInicial.split(','))
