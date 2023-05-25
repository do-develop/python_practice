from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 0
        self.gates = [Semaphore(), Semaphore(), Semaphore()] # even, odd, zero
        self.gates[0].acquire()
        self.gates[1].acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.cnt += 1
            self.gates[self.cnt % 2].release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.gates[0].acquire() # when semaphore open
            printNumber(self.cnt)
            self.gates[2].release() # fire print zero
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.gates[1].acquire()
            printNumber(self.cnt)
            self.gates[2].release()
