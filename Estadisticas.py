__author__ = ""


class Estadisticas:
    def calcular(self, cadenaInicial):
        response = []
        if cadenaInicial == "":
            response.append(0)
            response.append(None)
            response.append(None)
            return response
