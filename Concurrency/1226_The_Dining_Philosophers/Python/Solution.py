import threading

class DiningPhilosophers:
    def __init__(self):
        # number of philosophers
        self.numOfPhilosophers = 5
        # set up mutex locks
        self.forks = []
        for i in range(self.numOfPhilosophers):
            self.forks.append(threading.Lock())

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: 'Callable[[], None]',
        pickRightFork: 'Callable[[], None]',
        eat: 'Callable[[], None]',
        putLeftFork: 'Callable[[], None]',
        putRightFork: 'Callable[[], None]',
    ) -> None:
        # left and right forks
        leftForkIdx = (philosopher + 1) % self.numOfPhilosophers
        rightForkIdx = philosopher

        # divide order of fork acquiring to prevent deadlocks
        if philosopher % 2 == 0:
            # lock left fork and pick it up
            self.forks[leftForkIdx].acquire()
            pickLeftFork()
            # lock right fork and pick it up
            self.forks[rightForkIdx].acquire()
            pickRightFork()
        else:
            # lock right fork and pick it up
            self.forks[rightForkIdx].acquire()
            pickRightFork()
            # lock left fork and pick it up
            self.forks[leftForkIdx].acquire()
            pickLeftFork()

        # eat spaghetti
        eat()

        # unlock left fork and put it down
        putLeftFork()
        self.forks[leftForkIdx].release()
        # unlock right fork and put it down
        putRightFork()
        self.forks[rightForkIdx].release()
