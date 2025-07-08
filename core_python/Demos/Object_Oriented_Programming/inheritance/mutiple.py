class A:
    def display(self):
        print("Display method of class A")

class B:
    def display(self):
        print("Display method of class B")

class C(B, A):
    def show(self):
        print("Show method of class C.")

c1 = C()
c1.display()