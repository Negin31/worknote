class Warrior:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def hit(self, other):
        other.health -= 20
        print(self.name, ' атаковал ', other.name)
        if other.health <= 0:
            print(self.name, 'победил')


w1 = Warrior('war1')
w2 = Warrior('war2')

while (w1.health > 0) and (w2.health > 0):
    if w1.health < w2.health:
        w1.hit(w2)
    elif w2.health < w1.health:
        w2.hit(w1)
    else:
        w1.hit(w2)
