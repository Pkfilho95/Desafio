class computed_property:
    def __init__(self, *attrs): 
        self.fget = None
        self.fset = None
        self.fdel = None

        self.attrs = attrs
        self._cache = {}
        
        if attrs:
            self._cache = {attr:None for attr in attrs}
    
    def __call__(self, func):
        self.fget = func
        self.__doc__ = func.__doc__
        return self

    def __get__(self, instance, owner=None):
        if self.fget is None:
            raise AttributeError("Getter method not defined")
        
        if self._cache:
            for attr in self.attrs:
                if hasattr(instance, attr) and self._cache[attr] != getattr(instance, attr):
                    self._cache[attr] = getattr(instance, attr)
                    self._cache[self.fget.__name__] = self.fget(instance)
    
            return self._cache[self.fget.__name__]
        
        else:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Setter method not defined")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Deleter method not defined")
        self.fdel(instance)

    def getter(self, fget):
        self.fget = fget
        return self

    def setter(self, fset):
        self.fset = fset
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self
