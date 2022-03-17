import time
import threading

class FooBar():
    def __init__(self,n):
        self.n = n
    
    def foo(self):
        for _ in range(self.n):
            print("foo",end="")
            time.sleep(1)
    
    def bar(self):
        for _ in range(self.n):
            print("bar",end="")
            time.sleep(1)
    
    def yeah(self):
        for _ in range(self.n):
            print("yeah")
            time.sleep(1)

n = 3

fooBar = FooBar(n)

A = threading.Thread(target = fooBar.foo)
B = threading.Thread(target = fooBar.bar)
A.start()
B.start()
fooBar.yeah()
A.join()
B.join()