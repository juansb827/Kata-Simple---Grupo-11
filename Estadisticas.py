__author__ = ""


class Estadisticas:
    def calcular(self, cadenaInicial):
        response = []
        if cadenaInicial == "":
            response.append(0)
            response.append(None)
            response.append(None)
            response.append(None)
            return response
        else:
            array = map(int, cadenaInicial.split(','))
            response.append(len(array))
            response.append(int(min(array)))
            response.append(int(max(array)))
            response.append((float(sum(array)) / float(len(array))))
            return response
