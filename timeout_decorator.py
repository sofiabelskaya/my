import signal
import functools
from time import sleep


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super(TimeoutException, self).__init__(message)


def timeout(seconds=None):
    def timeout_dec(func):
        if seconds is None or seconds <= 0:
            return func
        else:
            def handler(signum, frame):
                raise TimeoutException("Timed out")

            @functools.wraps(func)
            def time_func(*args, **kwargs):
                signal.signal(signal.SIGALRM, handler)
                signal.setitimer(signal.ITIMER_REAL, seconds)
                try:
                    return func(*args, **kwargs)
                finally:
                    signal.setitimer(signal.ITIMER_REAL, 0)
                    signal.signal(signal.SIGALRM, signal.SIG_DFL)

        return time_func

    return timeout_dec
