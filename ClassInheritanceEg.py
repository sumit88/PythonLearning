class A:
    a = 0

    def __init__(self, a):
        print('constructor for A called')
        self.a = a

    def print_me(self):
        print('Hello from A')


class B(A):

    def __init__(self):
        print('Constructor of B called')

    #  A.__init__(self, 0)

    def print_me(self):
        print('Hello from B')


class C(B, A):
    pass


c = B()

c.print_me()
