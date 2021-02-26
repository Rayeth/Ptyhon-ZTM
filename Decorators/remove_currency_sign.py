def remove_sign_decorator(func):
    """ Removes currency sign """
    def wrap_func(x, sign):
        if sign in x:
            x = x.replace(sign, '')
            return func(x)
    return wrap_func
    
@remove_sign_decorator    
def value_to_float(x):
    
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

var = '€250M'
print(type(var))
print(value_to_float(var,'€'))

help(remove_sign_decorator)
print(remove_sign_decorator.__doc__)





