# *args: Positional Variable-Length Arguments
def add(*numbers):
    # print(numbers)
    # print(type(numbers))
    # print(numbers[0])
    addition = 0
    for n in numbers:
        addition += n
    return addition
    # return sum(numbers)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(number, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key in kwargs:
    #     print(key)
    # for (key, values) in kwargs.items():
    #     print(f"{key} : {values}")
    # print(kwargs["add"])

    number += kwargs["add"]
    number -= kwargs["subtract"]
    number *= kwargs["multiply"]
    number /= kwargs["divide"]

    print(number)


calculate(87, add=45, multiply=21, subtract=32, divide=10)


class Car:

    def __init__(self, **optional_arguments):
        self.name = optional_arguments.get("name")
        self.modal = optional_arguments.get("modal")
        self.color = optional_arguments.get("color")


car = Car(name="Rolls Royce", modal="Phantom")
print(car.name)
print(car.modal)
print(car.color)
