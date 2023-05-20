""" 
keep_lazy() decorator example
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



# compatibility.py
from __future__ import absolute_import, unicode_literals

import sys

from django.utils import six
from django.utils.functional import keep_lazy
from django.utils.text import Truncator, format_lazy


def string_concat(*strings):
    return format_lazy('{}' * len(strings), *strings)


def truncate_words(s, num, end_text='...'):
    truncate = end_text and ' %s' % end_text or ''
    return Truncator(s).words(num, truncate=truncate)


truncate_words = keep_lazy(truncate_words, six.text_type)




"""
Lazy class property decorator
Certainly! Here's an example of a lazy_class_property decorator in Python, which allows for lazy evaluation of class properties:
"""

import functools

def lazy_class_property(func):
    """Decorator to implement lazy evaluation of class properties."""

    @property
    @functools.wraps(func)
    def lazy_loader(cls):
        if not hasattr(cls, "_lazy_cache"):
            cls._lazy_cache = {}
        if func.__name__ not in cls._lazy_cache:
            cls._lazy_cache[func.__name__] = func(cls)
        return cls._lazy_cache[func.__name__]

    return lazy_loader

"""
To use this decorator, you can apply it to a class method that serves as a getter for a class property. The property will be computed lazily, meaning it will be evaluated only when accessed for the first time. Here's an example:
"""

class MyClass:
    @lazy_class_property
    def my_property(cls):
        print("Computing my_property...")
        return 42

# Accessing the class property triggers the lazy evaluation
print(MyClass.my_property)  # Computing my_property... 42

# Accessing the class property again does not recompute it
print(MyClass.my_property)  # 42

"""
In this example, the my_property method is decorated with @lazy_class_property. The first time MyClass.my_property is accessed, the decorator will execute the method and store the result in the _lazy_cache dictionary specific to the class. Subsequent accesses to MyClass.my_property will return the cached value without recomputing it.

The lazy_class_property decorator ensures that the property is evaluated lazily and shared among all instances of the class. If you need a per-instance lazy property, you can modify the decorator to store the cached values in an instance-specific dictionary instead of a class-level dictionary.
"""




