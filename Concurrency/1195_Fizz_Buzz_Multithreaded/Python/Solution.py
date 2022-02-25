import threading

class FizzBuzz:
    def __init__(self, n: int):
        # range or tokens
        self.n = n
        # flag indicating if token range iteration is complete
        self.done = False
        # fizz mutex
        self.fizzMutex = threading.Lock()
        self.fizzMutex.acquire()
        # buzz mutex
        self.buzzMutex = threading.Lock()
        self.buzzMutex.acquire()
        # fizzbuzz mutex
        self.fizzbuzzMutex = threading.Lock()
        self.fizzbuzzMutex.acquire()
        # number mutex
        self.numberMutex = threading.Lock()
        self.numberMutex.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            # lock fizz mutex
            self.fizzMutex.acquire()
            # exit loop if done
            if self.done:
                break
            # call fizz printer function
            printFizz()
            # unlock fizz mutex
            self.numberMutex.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            # lock buzz mutex
            self.buzzMutex.acquire()
            # exit loop if done
            if self.done:
                break
            # call buzz printer function
            printBuzz()
            # unlock buzz mutex
            self.numberMutex.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            # lock buzz mutex
            self.fizzbuzzMutex.acquire()
            # exit loop if done
            if self.done:
                break
            # call fizzbuzz printer function
            printFizzBuzz()
            # unlock fizzbuzz mutex
            self.numberMutex.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        # iterate over tokens
        for i in range(1, self.n + 1):
            # check if divisible by 3
            divisible_by_3 = i % 3 == 0
            # check if divisible by 5
            divisible_by_5 = i % 5 == 0
            if divisible_by_3 and divisible_by_5:
                # unlock fizzbuzz mutex
                self.fizzbuzzMutex.release()
                # lock number mutex
                self.numberMutex.acquire()
            elif divisible_by_3:
                # unlock fizz mutex
                self.fizzMutex.release()
                # lock number mutex
                self.numberMutex.acquire()
            elif divisible_by_5:
                # unlock buzz mutex
                self.buzzMutex.release()
                # lock number mutex
                self.numberMutex.acquire()
            else:
                printNumber(i)

        # signal iteration completed
        self.done = True
        # unlock all mutexes
        self.fizzMutex.release()
        self.buzzMutex.release()
        self.fizzbuzzMutex.release()
        self.numberMutex.release()
