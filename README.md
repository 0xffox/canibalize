## About
This package enables code reuse in non-inheritance way from existing classes,
effectively implementing traits-oriented programming pattern.

## Story
Once upon a time there was 
```python 
class AHealthyClass:
    def see(self):
        print('I can see')

    def walk(self):
        print('Walking around')

    def run(self):
        print('I can run')
```
and he decided to visit his grandma and bring her fresh-baked pie.

But little did he know there was couple of hungry zombies in his merry way 
waiting to chew on some bones. 

They were old decrepit zombies - not very fast nor particulary perseptive.
```python
from canibalize import infect

@infect
class Zombie1:
    def see():
        raise Exception('Arrgh') # he was a pirate, probably

@infect
class Zombie2:
    def walk():
        raise Exception("I've fallen and I can't get up!")
```

He walked closer and closer to the ambush and then zombies pounced at him. And
started eating him.
```python

Zombie1.nomnom(AHealthyClass, ['see', 'walk'])
Zombie2.nomnom(AHealthyClass, 'walk')
```

And then strange things started to happend. Zombie1 who took AHealthyClass eye, 
start seeing things. And both of them been munching on AHealthyClass legs gain 
ability of walking again!
```python
z1 = Zombie1()
z1.see()
>>> I can see

z2 = Zombie2()
z2.walk()
>>> Walking around

z1.walk()
>>> Walking around
```

The miracle is that AHealthyClass can still see and walk and even run. 
Maybe he was a spider in disguise.
```python
h1 = AHealthyClass()
h1.see()
>>> I can see

h1.walk()
>>> Walking around

```

And then they took each other's arms(who still had an arm) and walk()-ed into
a sunset, which was beutiful to see().

And live happily ever after.

And married each other, probably...

**The END**


## Seriously, though
Lets imagine you have some Library and some Code that uses that Library.
You have no controll of both of them, but you need to add/modify functionality 
to them.

For example, you add serialization/deserialization/validation/schema-generation 
to classes of that Library, for example with pydantic.

You cannot subclass from Library classes, because Code will not utilize
them(without rewriting it ofcause). The only real option you have is to write
facade for every class of the Library to add desired behaviour.

With canibalize you can extend Library becaviour without modifying nither
Library nor Code.

```python
from Libray import SomeClass
from Code import run

from canibalize import canibalize
from pydantic import BaseModel
from typing import List

class SomeSerialization:
    @classmethod
    def __get_validators__(cls):
        some_class_json_validators = [
            ... SomeClass specific validators
        ]
        for v in some_class_json_validators:
            yield v

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            ... # update schema based on cls logic
        )


canibalize(
    SomeClass,
    SomeSerialization, 
    ['__get_validators__', __modify_schema__', 'Config']
)

@dataclass
class ResultClass(BaseModel):
    results: List[SomeType]

some = SomeClass(result = [run(*v) for v in mah_values])

# now SomeClass correctly produces json_schema no matter how deep it nested
print(some.json_schema(indent=2)) 
```
