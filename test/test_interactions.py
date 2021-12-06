from unittest import TestCase
from canibalize import infect
from .some import Some, Donor, some_inst


class TestInteractions(TestCase):
    def test_some(self):
        infect(Some)
        Some.nomnom(Donor, ['run', 'look'])

        self.assertEqual(some_inst.run(), 'Oleg running!')
        self.assertEqual(some_inst.look(), 'Oleg looking!')


