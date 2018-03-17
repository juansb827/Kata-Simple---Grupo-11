from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        self.assertEqual(Estadisticas().calcular(""), 0, "Numero de elementos Cadena vacia")

    def test_num_elementos_uno(self):
        self.assertEqual(Estadisticas().calcular("1"), 1, "Numero de elementos cadena de 1 elemento")

    def test_num_elementos_dos(self):
        self.assertEqual(Estadisticas().calcular("1,2"), 2, "Numero de elementos cadena de 2 elemento")