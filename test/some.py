
from .some_some import Some

class Donor(object):
    def run(self):
        return f'{self.name} running!'

    def look(self):
        return f'{self.name} looking!'

some_inst = Some('Oleg', 47)


