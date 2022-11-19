class deco(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("before")
        return self.func(*args, **kwargs)


def deco_method(func):
    def wrapper(*args, **kwargs):
        print(f"before {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@deco
@deco_method
def divide_num(a, b):
    return a / b


print(divide_num(1,3))
