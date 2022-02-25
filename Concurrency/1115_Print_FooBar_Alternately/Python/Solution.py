import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        # mutex lock for foo()
        self.mutex1 = threading.Lock()
        # mutex lock for bar()
        self.mutex2 = threading.Lock()
        # lock mutex2
        self.mutex2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # wait till mutex1 is unlocked, then lock mutex1
            self.mutex1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            # unlock mutex2
            self.mutex2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # wait till mutex2 is unlocked, then lock mutex2
            self.mutex2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            # unlock mutex1
            self.mutex1.release()
