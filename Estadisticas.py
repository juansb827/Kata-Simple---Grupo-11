__author__ = ""


class Estadisticas:
    def calcular(self, cadenaInicial):
        response = []
        if cadenaInicial == "":
            response.append(0)
            response.append(None)
            return response
        else:
            array = cadenaInicial.split(',')
            response.append(len(array))
            response.append(int(min(array)))
        return response
