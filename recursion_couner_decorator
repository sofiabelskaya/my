import functools


def counter(func):
    @functools.wraps(func)
    def count_f(*args, **kwargs):
        if count_f.depth == 0:
            count_f.ncalls = 0
            count_f.rdepth = 0

        count_f.ncalls += 1
        count_f.depth += 1
        count_f.rdepth = max(count_f.rdepth, count_f.depth)
        result = func(*args, **kwargs)
        count_f.depth -= 1
        return result

    count_f.depth = 0
    count_f.rdepth = 0
    count_f.ncalls = 0
    return count_f
