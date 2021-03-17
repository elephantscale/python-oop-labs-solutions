_categories = []

class Vehicle:
    @classmethod
    def __init_subclass__(cls, retail=True, **kwargs):
		  super().__init_subclass__(**kwargs)
        if retail:
            _categories.append(cls)

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

class Tractor(Vehicle):
    pass

class SchoolBus(Vehicle, retail=False):
    pass

print(_categories)