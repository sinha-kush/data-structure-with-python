import unittest
class Deque:
    def __init__(self):
        self.d = []
        self.size = 5

    def add_right(self, n):
        self.d.append(n)

    def add_left(self,n):
        self.d.insert(0,n)

    def delete_right(self):
        self.d.pop()

    def delete_left(self):
        self.d.pop(0)

    def showelements(self):
        print(self.d)



d1 = Deque()
d1.add_right(1)
d1.add_right(2)
d1.add_left(3)
d1.add_left(4)
d1.delete_right()

d1.showelements()



class Checkdeque(unittest.TestCase):

    def test_add_right(self):
        d1 = Deque()
        d1.add_right(1)
        q1.add_right(2)
        self.assertEqual([1, 2], d1)

    def test_add_left(self):
        d1 = Deque()
        d1.add_left(3)
        q1.add_left(4)
        self.assertEqual([3, 4], d1)

    def test_delete_left(self):
        d1 = Deque()
        d1.pop(0)
        self.assertEqual([4], q1.q)

    def test_delete_right(self):
        d1 = Deque()
        d1.pop()
        self.assertEqual([3], q1.q)



if __name__ == "main":
    unittest.main()





