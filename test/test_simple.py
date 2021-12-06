from unittest import TestCase
from canibalize import infect

class TestSimple(TestCase):
    def test_local(self):
        class Predator(object):
            def __init__(self, name):
                self.name = name

        class Pray(object):
            def run(self):
                return f'{self.name} running!'

            def look(self):
                return f'{self.name} looking!'

        infect(Predator)

        Predator.nomnom(Pray, ['run', 'look'])

        p = Predator('Mikie')

        self.assertEqual(p.run(), 'Mikie running!')
        self.assertEqual(p.look(), 'Mikie looking!')

    def test_after_instance_creation(self):
        class Predator1(object):
            def __init__(self, name):
                self.name = name

        p = Predator1('Mikie')

        class Pray1(object):
            def run(self):
                return f'{self.name} running!'

            def look(self):
                return f'{self.name} looking!'

        infect(Predator1)

        Predator1.nomnom(Pray1, ['run', 'look'])


        self.assertEqual(p.run(), 'Mikie running!')
        self.assertEqual(p.look(), 'Mikie looking!')

