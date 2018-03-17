from unittest import TestCase

from Estadisticas import Estadisticas


class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        response = [0, None, None, None]
        self.assertEqual(Estadisticas().calcular(""), response, "Numero de elementos Cadena vacia")

    def test_num_elementos_cadena_uno(self):
        response = [1, 1, 1, 1]
        self.assertEqual(Estadisticas().calcular("1"), response, "Numero de elementos Cadena 1 elemento")

    def test_num_elementos_cadena_dos(self):
        response = [2, 2, 10, 6]
        self.assertEqual(Estadisticas().calcular("10,2"), response, "Numero de elementos Cadena 2 elemento")

    def test_num_elementos_cadena_N(self):
        self.assertEqual(Estadisticas().calcular("10,7,5,3,1"), [5, 1, 10, 5.2], "Numero de elementos Cadena N elementos")
        self.assertEqual(Estadisticas().calcular("10,10,10,10,10"), [5, 10, 10, 10],
                         "Numero de elementos Cadena N elementos")
        self.assertEqual(Estadisticas().calcular("1,1,1,1,1"), [5, 1, 1, 1], "Numero de elementos Cadena N elementos")
