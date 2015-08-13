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


print(filter(lambda i: i%2 == 0, range(10)))
print(my_filter(lambda i: i%2 == 0, range(10)))
print(my_sum(range(6)))
print(my_reduce(operator.add, range(6)))
print(zip(['a', 'b', 'c'], [2, 3]))
print(my_zip(['a', 'b', 'c'], [2, 3]))
print(map(lambda x: x*2, ['a', 'b', 'c']))
print(my_map(lambda x: x*2, ['a', 'b', 'c']))
