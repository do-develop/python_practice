from threading import Semaphore
# semaphore approach is very similar to using lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_gate = Semaphore(1) # foo will print first
        self.bar_gate = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()
