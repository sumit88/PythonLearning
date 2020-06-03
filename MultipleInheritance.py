class A():
    def __init__(self , name):
        self.a = name
        print("Object A is initialized")

    def a_print_name(self):
        print(self.name)

class B():
    def __init__(self, name ):
        self.b = name
        print("Object B is initialized")

    def b_print_name(self):
            print(self.b)

class C(A,B):

    def __init__(self , c , b ,a):
        B.__init__(self,b)
        A.__init__(self, a)
        self.c = c
        print("Object C is initialized")

c  = C("ObjectC" , "ObjectB" , "ObjectA" )
pass

c.b_print_name()
c.b_print_name()
c.b_print_name()

