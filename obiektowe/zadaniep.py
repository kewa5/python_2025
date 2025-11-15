class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x +=x
        self.y +=y


if __name__ == '__main__':

    p = Punkt(2, 5)
    print (p.x, p.y)
    q = Punkt(3, 7)
    q.x += 4
    q.y += 6
    d = Punkt()
    d.move(4,1)

    print(p.x, p.y)
    print(q.x,q.y)
    print(d.x, d.y)
