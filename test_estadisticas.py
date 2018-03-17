from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        response = [0, None]
        self.assertEqual(Estadisticas().calcular(""), response, "Numero de elementos Cadena vacia")

    def test_num_elementos_uno(self):
        response = [1, 1]
        self.assertEqual(Estadisticas().calcular("1"), response, "Numero de elementos cadena de 1 elemento")

    def test_num_elementos_dos(self):
        response = [2, 1]
        self.assertEqual(Estadisticas().calcular("4, 1"), response, "Numero de elementos cadena de 2 elemento")

    def test_num_elementos_N(self):
        self.assertEqual(Estadisticas().calcular("1,2,3,4,5,6"), [6,1], "Numero de elementos cadena de N elemento")
        self.assertEqual(Estadisticas().calcular("1,2,3"), [3, 1], "Numero de elementos cadena de N elemento")
        self.assertEqual(Estadisticas().calcular("4,5,6"), [3, 4], "Numero de elementos cadena de N elemento")