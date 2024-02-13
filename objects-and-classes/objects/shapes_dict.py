import math

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": square_perimeter,
        "area": square_area
    }


def circle_perimeter(thing):
    return 2 * math.pi * thing["side"]

def circle_squar_area(thing):
    return thing["side"] ** 2

def circle_new(name, side):
    return {
        "name": name,
        "side": side,
        "perimeter": circle_perimeter,
        "area": circle_squar_area
    }



def call(thing, method_name):
    return thing[method_name](thing)



examples = [square_new("sq", 3), square_new("ci", 2)]
for thing in examples:
    n = thing["name"]
    p = call(thing, "perimeter")
    a = call(thing, "area")
    print(f"{n} has perimeter {p:.2f} and area {a:.2f}")