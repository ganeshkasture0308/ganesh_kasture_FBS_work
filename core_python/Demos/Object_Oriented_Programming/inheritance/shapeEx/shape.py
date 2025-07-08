class Shape:
    def __init__(self, id, area):
        self.id = id
        self.area = area

    def display(self):
        print("ID:", self.id)
        print("Area:", self.area)

# s = Shape('s1', 400)
# s.display()