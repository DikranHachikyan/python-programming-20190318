#!/home/wizard/anaconda3/bin/python

class Const:
    def __setattr__(self,attr,value):
        if attr in self.__dict__:
            raise ValueError('Cannot change const attribute')
        self.__dict__[attr] = value

    def __delattr__(self,attr):
        if attr in self.__dict__:
            raise ValueError('Cannot delete const attribute')
        raise AttributeError(f'Object {self.__class__.__name__} has not attribute {attr}')

if __name__ == '__main__':
    const = Const()
    const.PORT = 3000
    print(f'Port:{const.PORT}')
    # const.PORT = 4000
    # del const.PORT