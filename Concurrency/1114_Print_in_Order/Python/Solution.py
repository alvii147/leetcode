import threading

class Foo:
    def __init__(self):
        # mutex lock for first() and second()
        self.mutex1 = threading.Lock()
        # lock mutex1
        self.mutex1.acquire()
        # mutex lock for second() and third()
        self.mutex2 = threading.Lock()
        # lock mutex2
        self.mutex2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # unlock mutex1
        self.mutex1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # wait till mutex1 is unlocked, then lock mutex1
        self.mutex1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        # unlock mutex1
        self.mutex1.release()
        # unlock mutex2
        self.mutex2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # wait till mutex1 is unlocked, then lock mutex1
        self.mutex2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        # unlock mutex2
        self.mutex2.release()
