import unittest

from adventure import Hero


class TestSuiteHero(unittest.TestCase):
    def test_name_cant_be_blank(self):
        with self.assertRaises(TypeError):
            Hero("")

    def test_name_cant_be_int(self):
        with self.assertRaises(TypeError):
            Hero(1)

    def test_name_is_str(self):
        hero_name = 'placeholder'
        hero = Hero(hero_name)
        self.assertEqual(hero.name, hero_name)


if __name__ == '__main__':
    unittest.main()
