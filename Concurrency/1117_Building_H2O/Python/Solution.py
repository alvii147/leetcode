import threading

class H2O:
    def __init__(self):
        # hydrogen molecule count
        self.hydrogen_count = 0
        # oxygen molecule count
        self.oxygen_count = 0
        # mutex for r/w synchronization of hydrogen/oxygen counts
        self.mtx = threading.Lock()

    # bond hydrogen & oxygen molecules if possible
    def bond(self):
        # lock mutex
        self.mtx.acquire()
        # if water can be formed, clear hydrogen & oxygen counts
        if self.hydrogen_count == 2 and self.oxygen_count == 1:
            self.hydrogen_count = 0
            self.oxygen_count = 0
        # unlock mutex
        self.mtx.release()

    # hydrogen molecule function
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # loop exit condition
        exit_loop = False

        while not exit_loop:
            # lock mutex
            self.mtx.acquire()
            if self.hydrogen_count < 2:
                # increment hydrogen count if space available
                self.hydrogen_count += 1
                # releaseHydrogen() outputs "H". Do not change or remove this line.
                releaseHydrogen()
                # exit loop
                exit_loop = True

            # unlock mutex
            self.mtx.release()

        # bond molecules if possible
        self.bond()

    # oxygen molecule function
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # loop exit condition
        exit_loop = False

        while not exit_loop:
            # lock mutex
            self.mtx.acquire()
            if self.oxygen_count < 1:
                # increment oxygen count if space available
                self.oxygen_count += 1
                # releaseOxygen() outputs "O". Do not change or remove this line.
                releaseOxygen()
                # exit loop
                exit_loop = True

            # unlock mutex
            self.mtx.release()

        # bond molecules if possible
        self.bond()