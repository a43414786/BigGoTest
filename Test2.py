import time
import threading


class FooBar():
    def __init__(self,n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.yeah_lock = threading.Lock()
        self.bar_lock.acquire()
        self.yeah_lock.acquire()
    
    def foo(self):
        for _ in range(self.n):
            self.foo_lock.acquire()
            print("foo",end="")
            self.bar_lock.release()
    
    def bar(self):
        for _ in range(self.n):
            self.bar_lock.acquire()
            print("bar",end="")
            self.yeah_lock.release()
    
    def yeah(self):
        for _ in range(self.n):
            self.yeah_lock.acquire()
            print("yeah")
            self.foo_lock.release()

def main():
    n = 3

    fooBar = FooBar(n)

    A = threading.Thread(target = fooBar.foo)
    B = threading.Thread(target = fooBar.bar)
    A.start()
    B.start()
    fooBar.yeah()
    A.join()
    B.join()


if __name__ == "__main__":
    main()