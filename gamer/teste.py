
import gamer

from gamer import area

class TesteArea(unittest.TestCase):
    def teste_area_positivo(self):
        ar = area(10,10)
        self.assertEqual(ar,100)

    def teste_area_tipo_errado(self):
        with self.assertRaises(TypeError):
            ar=area('10',10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
