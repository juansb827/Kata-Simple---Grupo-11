from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        self.assertEqual(Estadisticas().calcular(""), 0, "Numero de elementos Cadena vacia")
