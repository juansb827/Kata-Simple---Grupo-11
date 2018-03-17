from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        response = [0, None]
        self.assertEqual(Estadisticas().calcular(""), response, "Numero de elementos Cadena vacia")

    def test_num_elementos_uno(self):
        response = [1, 1]
        self.assertEqual(Estadisticas().calcular("1"), response, "Numero de elementos cadena de 1 elemento")


