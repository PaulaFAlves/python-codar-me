from audioop import mul
from calculadora import somar, dividir, multiplicar, subtrair
import unittest

class TestSomar(unittest.TestCase):
  def testa_soma_de_dois_numeros_inteiros(self):
    self.assertEqual(somar(1, 2), 3)

  def testa_soma_de_numero_com_zero(self):
    self.assertEqual(somar(2, 0), 2)

class TestDividir(unittest.TestCase):
  def testa_divide_numero_por_1_retorna_o_numero(self):
    self.assertEqual(dividir(12, 1), 12)

  def testa_numero_divide_por_zero_igual_nan(self):
    self.assertEqual(dividir(12, 0), 'NAN')

  def testa_divide_dois_numeros(self):
    self.assertEqual(dividir(2, 5), 0.4)

class TestMultiplicar(unittest.TestCase):
  def testa_multiplica_numero_por_0_retorna_none(self):
    self.assertEqual(multiplicar(1, 0), 'None')

  def testa_multiplica_dois_numeros_inteiros(self):
    self.assertEqual(multiplicar(2, 3), 6)

  def testa_multiplica_numero_negativo_e_numero_positivo(self):
    self.assertEqual(multiplicar(-3, 6), -18)

  def testa_multiplica_numero_positivo_e_numero_negativo(self):
    self.assertEqual(multiplicar(5, -5), -25)

class TestSubtrair(unittest.TestCase):
  def testa_dimunui_dois_numeros_inteiros(self):
    self.assertEqual(subtrair(4, 1), 3)

  def testa_dimunui_numero_menor_e_numero_maior(self):
    self.assertEqual(subtrair(1, 4), -3)

  def testa_dimunui_numeros_negativos(self):
    self.assertEqual(subtrair(-5, -2), -3)

unittest.main()