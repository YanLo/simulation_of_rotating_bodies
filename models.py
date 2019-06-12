#there models are described as diff equation like x' = f(x)
import functools


def oscillation(x, w, b):
    #x[0] = x, x[1] = v             x' = v
    #x'' = -b * v -w^2 * x   <=>    v' = -b * v -w^2 * x
    return [x[1], -b * x[1] -w**2 * x[0]]

# we need decorator here because we want to get function which depends only of x
# as it used in integration methods later


def model_decorator(params):
    w = params[0]
    b = params[1]
    def decorator(func):
        @functools.wraps(func)
        def wrapped(x):
            result = func(x, b, w)
            return result
        return wrapped
    return decorator