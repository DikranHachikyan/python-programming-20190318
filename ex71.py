#!/home/wizard/anaconda3/bin/python
class A:
    def __init__(self,scale):
        self._scale = scale

    def showA(self):
        print(f'A scale:{self._scale}')

class B(A):

    def showB(self,scale):
        self._scale = scale
        print(f'B scale:{self._scale}')

if __name__ == '__main__':
    obj = B(100)

    obj.showA()
    obj.showB(5)
    obj.showA()

    print(obj.__dict__.keys())