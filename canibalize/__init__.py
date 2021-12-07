from typing import Type, Callable
from collections import defaultdict

def canibalize(predator: Type, pray: Type, attr_list=None):
    ''' Enable your class (@predator) to use other class' (@pray)
        methods from @attr_list
    '''
    # init default values
    if attr_list is None:
        attr_list = []
    elif not isinstance(attr_list, list):
        attr_list = [attr_list, ]

    # history
    if not hasattr(predator, '__canibalized__'):
        setattr(predator, '__canibalized__', defaultdict(lambda: set()))

    # Nomnomnoming
    for attr_name in attr_list:
        if hasattr(pray, attr_name):
            setattr(predator, attr_name, getattr(pray, attr_name))
            predator.__canibalized__[pray].add(attr_name)


def infect(what:Type):
    ''' Enable your class to chew on other classes with .nomnom() method
    '''
    @classmethod
    def _(this, that, attr_list=None):
        canibalize(this, that, attr_list)

    setattr(what, 'nomnom', _)
    return what
