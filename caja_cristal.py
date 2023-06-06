import unittest

def es_mayor_de_edad(edad):
    return edad >= 18

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)

    def test_es_menor(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()
