_categories = []

class Vehicle:
    @classmethod
    def __init_subclass__(cls, **kwargs):
			super().__init_subclass__(**kwargs)
        _categories.append(cls)

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

class Tractor(Vehicle):
    pass

print(_categories)