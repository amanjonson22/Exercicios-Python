class Foo:
    def __init__(self, x = None):
        self._x = x

    @property #pega o método e torna em atributo
    def x(self):
        return self._x or 0
    
    @x.setter #para setar x, sem ele não consigo fazer foo.x = y
    def x(self, value):
        #return self._x + value ---> não funciona pois não é um método
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x) 