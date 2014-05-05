"""
decorators.py

Module for custom decorators
"""

import inspect
import logging

LOGGER = logging.getLogger(__name__)

def log(function):
    """
    This decorator will add logging information to instance methods.

    For example:
        INFO - Entering class.method()
        DEBUG - function arguments: args=() | kwargs=()
        DEBUG - Exiting class.method()

    It should not be used for class methods, static methods, or module
    methods.
    """
    def return_function(*args, **kwargs):
        arg_spec = inspect.getargspec(function)
        # Assuming the function has a self arg, the function is bound to a class
        if 'self' in arg_spec.args:
            cls = args[0].__class__
        LOGGER.info('Entering {}.{}()'.format(cls.__name__, function.__name__))
        LOGGER.debug('function arguments: args={} | kwargs={}'.format(args, kwargs))
        f_result = function(*args, **kwargs)
        LOGGER.debug('Exiting {}.{}()'.format(cls.__name__, function.__name__))
        return f_result
    # Preserve function name
    return_function.__name__ = function.__name__
    return return_function
