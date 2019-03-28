#!/home/wizard/anaconda3/bin/python

def show(title, *args, kw1='A', kw2='B' ,**kwargs):
    print(f'Title:{title}')
    print(f'kw1:{kw1} , kw2:{kw2}')

def show2(title, *, kw1='A', kw2='B'):
    print(f'Title:{title}')
    print(f'kw1:{kw1} , kw2:{kw2}')
      

if __name__ == '__main__':
    show('Text Editor',kw1='C')
    show2('Python App', kw2='X', kw1='C')
