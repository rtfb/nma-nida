import operator


def my_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + my_sum(lst[1:])


def my_map(func, lst):
    if not lst:
        return []
    return [func(lst[0])] + my_map(func, lst[1:])


def my_filter(pred, lst):
    if not lst:
        return []
    return ([lst[0]] if pred(lst[0]) else []) + my_filter(pred, lst[1:])


def my_zip(lst1, lst2):
    if not lst1 or not lst2:
        return []
    return [(lst1[0], lst2[0])] + my_zip(lst1[1:], lst2[1:])


def my_reduce(func, lst):
    if len(lst) < 2:
        return lst[0]
    return func(lst[0], my_reduce(func, lst[1:]))


def flat_trace(f):
    def g(x):
        print(f.__name__, x)
        value = f(x)
        print('return', repr(value))
        return value
    return g


def trace(f):
    f.indent = 0
    def g(x):
        print '|  ' * f.indent + '|--', f.__name__, x
        f.indent += 1
        value = f(x)
        print '|  ' * f.indent + '|--', 'return', repr(value)
        f.indent -= 1
        return value
    return g


def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])


@trace
def mergesort(lst):
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[1] < lst[0]:
            return [lst[1], lst[0]]
        else:
            return lst
    mid = len(lst) / 2
    left = lst[:mid]
    right = lst[mid:]
    return merge(mergesort(left), mergesort(right))


"""
>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}


>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}


>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
"""


print(filter(lambda i: i%2 == 0, range(10)))
print(my_filter(lambda i: i%2 == 0, range(10)))
print(my_sum(range(6)))
print(my_reduce(operator.add, range(6)))
print(zip(['a', 'b', 'c'], [2, 3]))
print(my_zip(['a', 'b', 'c'], [2, 3]))
print(map(lambda x: x*2, ['a', 'b', 'c']))
print(my_map(lambda x: x*2, ['a', 'b', 'c']))
print('---')
l1 = [2, 4, 6]
l2 = [3, 5, 7, 10]
print(merge(l1, l2))
print(merge([1, 4, 17], []))
print(merge([], [1, 4, 17]))
print(merge([1], [1, 4]))
print(merge([1, 2], [4]))
print(merge([1, 2], [1]))
print('====')
l = [5, 2, 7, 32, 1, 56, 4, 6, 5, 4, 65, 54, 6, 45]
#l = [32, 1, 56, 4]
print('l = ', l)
print(sorted(l))
print(mergesort(l))


@trace
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib = trace(fib)
print(fib(3))

"""
>>> def square(x): return x * x
...
>>> f = vectorize(square)
>>> f([1, 2, 3])
[1, 4, 9]
"""
