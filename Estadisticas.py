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
        elif len(cadenaInicial) == 1:
            array = cadenaInicial.split(',')
            response.append(len(array))
            response.append(int(min(array)))
            response.append(int(max(array)))
            response.append(int(min(array)))
            return response
        elif len(cadenaInicial) == 4:
            array = cadenaInicial.split(',')
            response.append(len(array))
            response.append(int(min(array)))
            response.append(int(max(array)))
            return response
        else:
            array = map(int, cadenaInicial.split(','))
            response.append(len(array))
            response.append(int(min(array)))
            response.append(int(max(array)))
            return response
