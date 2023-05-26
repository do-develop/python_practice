from threading import Barrier, Semaphore
class H2O:
    def __init__(self):
        self.bar = Barrier(3)
        self.hydro = Semaphore(2)
        self.oxy = Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydro.acquire()
        self.bar.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydro.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxy.acquire()
        self.bar.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oxy.release()
