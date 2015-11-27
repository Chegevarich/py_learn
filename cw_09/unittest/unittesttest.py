#coding:utf-8
import unittest

class TestStringMethods(unittest.TestCase):

  #test0
  def test_upper(self):# имя начинается с test_
      #self.assertEqual('foo'.upper(), 'FOO')
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

class TestStringMethods2(unittest.TestCase):
  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()