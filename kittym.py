import math

def funclist(s):
    f = {
        'fabs': [
            'fabs(x)',
            'return the absolute value of x, where x is a number and the absolute value is always a float',
            'fabs(-3)', '', 'math'
        ],
        'abs': [
            'abs(x)', 'return the absolute value of x, where x is a number',
            'abs(-3)', '', ''
        ],
        'ceiling': [
            'ceiling(x)', 'return the ceiling of x', 'ceiling(3.3)', 'ceil',
            'math'
        ],
        'ceil':
        ['ceil(x)', 'return the ceiling of x', 'ceil(3.3)', '', 'math'],
        'floor': [
            'floor(x)',
            'return the floor of x, where x is a number and floor is an integer',
            'floor(3.8)', '', 'math'
        ],
        'trunc':
        ['trunc(x)', 'return the integer of x', 'trunc(3.8)', '', 'math'],
        'int': ['int(x)', 'return the integer of x', 'int(3.8)', '', ''],
        'gcd': [
            'gcd(x,y)',
            'return the greatest common divisor of x and y',
            'gcd(8,12)', '', 'math'
        ],
        'hcf': [
            'hcf(x,y)', 'return the highest common divisor of x and y and ...',
            'hcf(4,8)', 'gcd', 'math'
        ],
        #'lcm': [
        #    'lcm(x,y)', 'return the lowest common multiple of x and y and ...',
        #    'lcm(3,8,4)', '', 'math'
        #],
        'frexp': [
            'frexp(x)',
            'return the (mantissa, exponent) of x, where x = mantissa*(2^exponent)',
            'frexp(30)', '', 'math'
        ],
        'ldexp': ['ldexp(x,y)', 'return x*2^y', 'ldexp(3,2)', '', 'math'],
        'remainder': [
            'rem(x,y)',
            'return the IEEE 754 remainder, which is the difference of x - n*y, where n is the closest integer to x/y',
            'remainder(3,4)', '', 'math'
        ],
        'irem': [
            'irem(x,y)',
            'return the IEEE 754 remainder, which is the difference of x - n*y, where n is the closest integer to x/y',
            'rem(3,4)', 'remainder', 'math'
        ],
        'fmod':
        ['fmod(x,y)', 'return the remainder of x/y', 'fmod(3,4)', '', 'math'],
        'modf': [
            'modf(x)', 'return the fractional and integer parts of x',
            'modf(5/4)', '', 'math'
        ],
        'mod': [
            'mod(x,y)', 'return the remainder of x/y', 'mod(3,4)', 'cus_mod',
            'self'
        ],
        'rem': [
            'rem(x,y)', 'return the remainder of x/y, same as mod', 'rem(3,4)',
            'cus_mod', 'self'
        ],
        'fsum': [
            'fsum(x)', 'return the sum of x, where x is a list of numbers',
            'fsum([1,2,3])', '', 'math'
        ],
        'prod': [
            'prod(x)', 'return the product of x, where x is a list of numbers',
            'prod([1,2,3])', '', 'math'
        ],
        'factorial': [
            'factorial(n)',
            'return n factorial, where n is a positive integer',
            'factorial(5)', '', 'math'
        ],
        'perm': [
            'perm(n,k)',
            'return the number of arrangements of k objects from n different objects',
            'perm(5,3)', '', 'math'
        ],
        'comb': [
            'comb(n,k)',
            'return the number of combinations of k objects from n different objects',
            'comb(5,3)', '', 'math'
        ],
        'asinh': [
            'asinh(x)', 'return the inverse hyperbolic sine of x', 'asinh(3)',
            '', 'math'
        ],
        'acosh': [
            'acosh(x)', 'return the inverse hyperbolic cosine of x',
            'acosh(3)', '', 'math'
        ],
        'atanh': [
            'atanh(x)', 'return the inverse hyperbolic tangent of x',
            'atanh(0.3)', '', 'math'
        ],
        'sinh':
        ['sinh(x)', 'return the hyperbolic sine of x', 'sinh(3)', '', 'math'],
        'cosh': [
            'cosh(x)', 'return the hyperbolic cosine of x', 'cosh(3)', '',
            'math'
        ],
        'tanh': [
            'tanh(x)', 'return the hyperbolic tangent of x', 'tanh(3)', '',
            'math'
        ],
        'asind': [
            'asind(x)', 'return the arc sine of x in degrees', 'asind(0.5)',
            'cus_asind', 'self'
        ],
        'acosd': [
            'acosd(x)', 'return the arc cosine of x in degrees', 'acosd(0.5)',
            'cus_acosd', 'self'
        ],
        'atand': [
            'atand(x)', 'return the arc tangent of x in degrees', 'atand(0.5)',
            'cus_atand', 'self'
        ],
        'sind': [
            'sind(x)', 'return the sine of x, where x is in degrees',
            'sind(30)', 'cus_sind', 'self'
        ],
        'cosd': [
            'cosd(x)', 'return the cosine of x, where x is in degrees',
            'cosd(30)', 'cus_cosd', 'self'
        ],
        'tand': [
            'tand(x)', 'return the tangent of x, where x is in degrees',
            'tand(30)', 'cus_tand', 'self'
        ],
        'atan2': [
            'atan2(x,y)',
            'return the angle in radians between the line made by the point (x,y) and the origin, with the positive x-axis',
            'atan2(-1,-1)', '', 'math'
        ],
        'atand2': [
            'atan2(x,y)',
            'return the angle in degrees between the line made by the point (x,y) and the origin, with the positive x-axis',
            'atand2(-1,-1)', 'cus_atand2', 'self'
        ],
        'asind3': [
            'asind3(x)',
            'return the arc sine of x in degrees and in their respective quadrants',
            'asind3(-0.5)', 'cus_asind3', 'self'
        ],
        'acosd3': [
            'acosd3(x)',
            'return the arc sine of x in degrees and in their respective quadrants',
            'acosd3(-0.5)', 'cus_acosd3', 'self'
        ],
        'atand3': [
            'atand3(x)',
            'return the arc sine of x in degrees and in their respective quadrants',
            'atand3(-0.5)', 'cus_atand3', 'self'
        ],
        'asin': [
            'asin(x)', 'return the arc sine of x in radians', 'sin(0.3)', '',
            'math'
        ],
        'acos': [
            'acos(x)', 'return the arc cosine of x in radians', 'cos(0.3)', '',
            'math'
        ],
        'atan': [
            'atan(x)', 'return the arc tangent of x in radian', 'atan(0.3)',
            '', 'math'
        ],
        'sin': [
            'sin(x)', 'return the sine of x, where x is in radians', 'sin(3)',
            '', 'math'
        ],
        'cos': [
            'cos(x)', 'return the cosine of x, where x is in radians',
            'cos(3)', '', 'math'
        ],
        'tan': [
            'tan(x)', 'return the tangent of x, where x is in radians',
            'tan(3)', '', 'math'
        ],
        'degrees': [
            'degrees(x)', 'convert x in radians to degrees', 'degrees(3)', '',
            'math'
        ],
        'degree': [
            'degree(x)', 'convert x in radians to degrees', 'degree(3)',
            'degrees', 'math'
        ],
        'deg': [
            'deg(x)', 'convert x in radians to degrees', 'deg(3)', 'degrees',
            'math'
        ],
        'radians': [
            'radians(x)', 'convert x in degrees to radians', 'radians(3)', '',
            'math'
        ],
        'radian': [
            'radian(x)', 'convert x in degrees to radians', 'radian(3)',
            'radians', 'math'
        ],
        'rad': [
            'rad(x)', 'convert x in degrees to radians', 'rad(3)', 'radians',
            'math'
        ],
        'exp': ['exp(x)', 'return e to the power of x', 'exp(3)', '', 'math'],
        'expm1': [
            'expm1(x)', 'exp(x) - 1, use when x is really small',
            'expm1(1e-5)', '', 'math'
        ],
        'log1p': [
            'log1p(x)',
            'return the natural logarithm of x (base e); for x near zero',
            'log1p(1e-9)', '', 'math'
        ],
        'log10': [
            'log10(x)', 'return the logarithm of x to base 10', 'log10(8)', '',
            'math'
        ],
        'log2': [
            'log2(x)', 'return the logarithm of x to base 2', 'log2(8)', '',
            'math'
        ],
        'log': [
            'log(x,y)',
            'return the logarithm of x to the base y; if y is omitted, return the natural logarithm of x (base e)',
            'log(8,2)', '', 'math'
        ],
        'fpow': [
            'fpow(x,y)', 'return x to the power of y', 'fpow(2,3)', 'pow',
            'math'
        ],
        'pow': ['pow(x,y)', 'return x to the power of y', 'pow(2,3)', '', ''],
        'sqrt':
        ['sqrt(x)', 'return the square root of x', 'sqrt(3)', '', 'math'],
        'cbrt': [
            'cbrt(x)', 'return the cube root of x', 'cbrt(3)', 'cus_cbrt',
            'self'
        ],
        'pi': ['pi', 'return the constant pi', 'pi()', 'cus_pi', 'self'],
        'e': ['e', 'return the constant e', 'e()', 'cus_e', 'self'],
    }

    #enumerate f
    j = 1
    for i in f:
        f[i].append('f' + str(j))
        j = j + 1

    vlen = len(f['sin'])

    if s in f:
        return f[s]
    elif s == 'allkeys':
        return f.keys()
    elif s == 'allkeyfids':
        d = {}
        for k, v in f.items():
            d[k] = v[vlen - 1]
        return d
    elif s == 'allfidkeys':
        d = {}
        for k, v in f.items():
            d[v[vlen - 1]] = k
        return d
    elif s == 'allfidpys':
        d = {}
        for k, v in f.items():
            if v[3] == '':
                d[v[vlen - 1]] = k
            else:
                d[v[vlen - 1]] = v[3]
            if v[4] != '':
                d[v[vlen - 1]] = v[4] + '.' + d[v[vlen - 1]]
        return d
    elif s[:3] == 'fid':
        s = s[4:].rstrip(')')
        return f[s][vlen - 1]
    else:
        return 'The function is not in the list.'


def rep_funcname(fn):
    a = funclist('allkeyfids')
    for i in a:
        j = i + '('
        if j in fn:
            fn = fn.replace(j, a[i] + '(')

    a = funclist('allfidpys')
    for i in a:
        j = i + '('
        if j in fn:
            fn = fn.replace(j, a[i] + '(')
    return fn


def eval_py(s):
    s = rep_funcname(s)
    if s[:4] == 'self':
        s = s[5:]
        return eval(s)
    try:
        return eval(s)
    except Exception as e:
        if hasattr(e, 'message'):
            return e.message
        else:
            return str(e)


def cus_sind(x):
    return math.sin(math.radians(x))


def cus_cosd(x):
    return math.cos(math.radians(x))


def cus_tand(x):
    return math.tan(math.radians(x))


def cus_asind(x):
    return math.degrees(math.asin(x))


def cus_acosd(x):
    return math.degrees(math.acos(x))


def cus_atand(x):
    return math.degrees(math.atan(x))


def cus_atand2(x, y):
    return math.degrees(math.atan2(x, y))


def cus_asind3(x):
    if x == 1:
        return 90
    elif x == -1:
        return 270
    elif x == 0:
        return (0, 180, 360)
    elif x > 0:
        y = math.degrees(math.asin(x))
        return (y, 180 - y)
    elif x < 0:
        y = math.degrees(math.asin(-x))
        return (180 + y, 360 - y)


def cus_acosd3(x):
    if x == 1:
        return (0, 360)
    elif x == -1:
        return 180
    elif x == 0:
        return (90, 270)
    elif x > 0:
        y = math.degrees(math.acos(x))
        return (y, 360 - y)
    elif x < 0:
        y = math.degrees(math.acos(-x))
        return (180 - y, 180 + y)


def cus_atand3(x):
    if x == 0:
        return (0, 180, 360)
    elif x > 0:
        y = math.degrees(math.atan(x))
        return (y, 180 + y)
    elif x < 0:
        y = math.degrees(math.atan(-x))
        return (180 - y, 360 - y)


def cus_mod(x, y):
    return x % y


def cus_cbrt(x):
    if x > 0:
        return math.pow(x, 1 / 3)
    elif x < 0:
        return -math.pow(-x, 1 / 3)
    else:
        return 0


def cus_pi():
    return math.pi


def cus_e():
    return math.e


def kitty_help(s):
    #s is a string that starts with "Kitty help"
    #return text
    #format s here, query must be separated by 1 space only

    a = s.split(' ')

    if not (len(a) == 2 or len(a) == 3):
        return ''

    if a[1] == 'help':
        if len(a) == 2:
            h = ("Meeow. Currently, I can help you with these:\n"
                 "1) syntax\n"
                 "2) eval\n"
                 "3) calc\n"
                 "4) blog\n"
                 "Please type: Kitty help <topic_name>")
        elif a[2] == 'syntax':
            h = ("General syntax:\n"
                 "Kitty <keyword> <keyword> ... <expression>\n\nNote:\n"
                 "<keyword> = a word that Kitty understands, like help\n"
                 "... = and some more (of the previous)\n"
                 "<expression> = stuff to be computed, like sin(3)")
        elif a[2] == 'eval':
            h = ("eval <expression>\n"
                 "Evaluate the expression that follows it.\n"
                 "This function is based on Python's eval().\n"
                 "Example: Kitty eval sin(3) + 1\n\n")
            h = h + "Supported math：\n"
            f = funclist('allkeys')
            f = list(f)
            f.sort()
            f = '\t\t'.join(f) + "\n"
            h = h + f + ("\nFor more help, type:\n"
                         "\tKitty help <function>\n"
                         "Example: Kitty help sin\n")
        elif a[2] == 'calc':
            h = ("calc <expression>\n"
                 "Evaluate the expression that follows it.\n"
                 "This function is based on mathzilla.app's API.\n"
                 "Example: Kitty calc sin(3) + 1"
                 "\nWe are doing some stuff with this. Don't use, if possible.")
        elif a[2] == 'blog':
            h=("Recent blogs:\n"
                "Replit is getting slow at times (and long sleep time); alternative ...searching (21/6)\n"
                "Kitty was refused because she was asleep ... too bad.\n"
                "We have just submitted Kitty to top.gg (27/4)\n"
                "Math functions, mostly centered on high school maths added. We will keep adding. (18/4)\n"
                "Kitty says, 'I exist.'"
            )
        else:
            h = funclist(a[2])
            if type(h) == list:
                h = h[0] + "\n" + h[1] + "\nthus, " + h[2] + " returns " + str(
                    eval_py(h[2]))

    return h
