from unittest import TestCase
from canibalize import infect

class TestHistory(TestCase):
    def test_local(self):
        class Predator(object):
            def __init__(self, name):
                self.name = name

        class Runner(object):
            def run(self):
                return f'{self.name} running!'

        class Looker(object):
            def look(self):
                return f'{self.name} looking!'

        infect(Predator)
        Predator.nomnom(Runner, 'run')
        Predator.nomnom(Looker, 'look')

        p = Predator('Vasya')
        self.assertEqual(p.look(), 'Vasya looking!')
        self.assertEqual(p.run(), 'Vasya running!')

        self.assertIn(Runner, Predator.__canibalized__)
        self.assertIn(Looker, Predator.__canibalized__)

        self.assertIn('run', Predator.__canibalized__[Runner])
        self.assertIn('look', Predator.__canibalized__[Looker])


