# Decorator
import functools

def repeat(number):
    def repeatMe(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(number):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeatMe 


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
@repeat(6)
def name():
    print("Aniket")

name()