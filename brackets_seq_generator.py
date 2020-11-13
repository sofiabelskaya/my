def alg_brackets(n, n_open=0, n_close=0, seq=""):
    if n_open + n_close == 2 * n:
        yield seq
    if n_open < n:
        for count, new_seq in enumerate(alg_brackets(n, n_open + 1, n_close, seq + '(')):
            yield new_seq
    if n_open > n_close:
        for count, new_seq in enumerate(alg_brackets(n, n_open, n_close + 1, seq + ')')):
            yield new_seq


def brackets(n):
    for new_seq in alg_brackets(n):
        yield new_seq
