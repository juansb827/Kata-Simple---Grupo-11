from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):

    def test_num_elementos_cadena_vacia(self):
        response = [0, None, None]
        self.assertEqual(Estadisticas().calcular(""), response, "Numero de elementos Cadena vacia")