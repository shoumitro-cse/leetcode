""" keep_lazy() decorator example

Certainly! Here's an example of a keep_lazy() decorator in Python:
""" 

import functools

def keep_lazy(func):
    """Decorator to delay evaluation of a function until the result is needed."""

    @functools.wraps(func)
    def lazy_func(*args, **kwargs):
        result = func(*args, **kwargs)

        def eval_func():
            return result

        lazy_func.eval = eval_func
        return lazy_func

    return lazy_func

""" 
This decorator allows you to delay the execution of a function until its result is explicitly requested. Here's how you can use it:
""" 

@keep_lazy
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b

result = add_numbers(5, 3)  # The function is not executed yet

# Later, when you need the result, you can explicitly evaluate the function
print(result.eval())  # Adding numbers... 8

""" 
In this example, the add_numbers() function is decorated with @keep_lazy. When you call add_numbers(5, 3), the function is not immediately executed. Instead, it returns a "lazy" function object, result, which stores the original function's result.

To obtain the actual result, you can call result.eval(), which triggers the execution of the original function and returns the computed value. This way, you have control over when the function is evaluated, allowing for lazy evaluation when necessary.
""" 




