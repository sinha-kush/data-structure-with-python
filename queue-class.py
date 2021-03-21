import unittest


class Queue:
    def __init__(self):
        self.q = []
        self.size = 5

    def insert(self, n):
        self.q.append(n)

    def delete(self):
        self.q.pop(0)

    def isempty(self):
        if len(self.q) == 0:
            print("queue is empty")
        else:
            print("elements available")

    def showelements(self):
        print(self.q)


class Checkqueue(unittest.TestCase):
    def test_insert(self):
        q1 = Queue()
        q1.insert(1)
        q1.insert(2)
        self.assertEqual([1, 2], q1)

    def test_delete(self):
        q1 = Queue()
        q1.pop(0)
        self.assertEqual([1], q1.q)

    def test_isempty(self):
        q1 = Queue()
        q1.pop(0)
        q1.pop(0)
        self.assertRaises("Index Error", q1.pop())



if __name__ == "main":
    unittest.main()


