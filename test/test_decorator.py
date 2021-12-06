from unittest import TestCase
from canibalize import infect

class TestDecorator(TestCase):
    def test_decorator(self):

        # if you know that you'll be eating later 
        # you can create class already infected
        @infect
        class Predator(object):
            def __init__(self, name):
                self.name = name

        class Pray(object):
            def run(self):
                return f'{self.name} running!'

            def look(self):
                return f'{self.name} looking!'

        Predator.nomnom(Pray, ['run', 'look'])

        p = Predator('Leo')

        self.assertEqual(p.run(), 'Leo running!')
        self.assertEqual(p.look(), 'Leo looking!')

