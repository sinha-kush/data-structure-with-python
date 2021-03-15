import unittest
class Stack:
    def __init__(self):
         self.s = []
         self.size = 5

    def push(self,n):
        self.s.append(n)

    def pop(self):
        self.s.pop()

    def peek(self):
        print(self.s[0])

    def isempty(self):
        if len(self.s)==0:
            print("stack is empty")
        else:
            print("elements available")

    #def isfull(self):
        #if len(self.s)==self.size:
            #print("stack is full")
       # elif len(self.s) > self.size:
            #raise Exception("size exceeded")



s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.peek()
s1.isempty()


class Checktest(unittest.TestCase):


    def test_push1(self):
        s1 = Stack()
        s1.push(1)
        self.assertEqual([1], s1)

    def test_push2(self):
        s1 = Stack()
        s1.push(1)
        s1.push(2)
        self.assertEqual([1,2], s1)


    def test_pop1(self):
         s1 = Stack()
         s1.pop()
         self.assertEqual([1], s1.s)

    def test_popempty(self):
        s1 = Stack()
        s1.pop()
        s1.pop()
        self.assertRaises("Index Error", s1.pop())

    def test_peek(self):
        s1 = Stack()
        s1.peek(1)
        self.assertEqual([1], s1.peek())








if __name__ == "main":
    unittest.main()
