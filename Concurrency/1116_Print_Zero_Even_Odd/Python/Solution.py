import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        # mutex lock for zero()
        self.mutex_zero = threading.Lock()
        # mutex lock for even()
        self.mutex_even = threading.Lock()
        # mutex lock for odd()
        self.mutex_odd = threading.Lock()
        # lock mutex even
        self.mutex_even.acquire()
        # lock mutex odd
        self.mutex_odd.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            # wait till mutex zero is unlocked, then lock it
            self.mutex_zero.acquire()
            # print zero
            printNumber(0)
            # if index is odd
            if i % 2 == 1:
                # unlock mutex even
                self.mutex_even.release()
            else:
                # unlock mutex odd
                self.mutex_odd.release()

        # if n is odd, unlock mutex even
        if self.n % 2 == 1:
            # unlock mutex even
            self.mutex_even.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            # wait till mutex even is unlocked, then lock it
            self.mutex_even.acquire()
            # print even number
            printNumber(i)
            # unlock mutex zero
            self.mutex_zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            # wait till mutex odd is unlocked, then lock it
            self.mutex_odd.acquire()
            # print odd number
            printNumber(i)
            # unlock mutex zero
            self.mutex_zero.release()
