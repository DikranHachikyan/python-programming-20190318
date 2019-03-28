#!/home/wizard/anaconda3/bin/python

def show(title, *args, **kwargs):
    print(f'Title:{title}')

    print('Args:')
    for v in args:
        print(f'arg:{v}')

    params = {
          'path' : kwargs.get('path','/tmp')
        , 'log': kwargs.get('log','/var/log/messages') 
    }
    print(f'params:{params}')    

if __name__ == '__main__':
    show('Text Editor')

    show('Text Editor', 1, 2, 200, 4000)

    show('Text Editor', 1, 2, 200, 4000,log='/var/log/app.log',path='/usr/bin')
    
    appSettings = {
          'path':'/usr/local/bin'
        , 'author':'anna'
        , 'mem': 4096
    }

    show('Text Editor', 1, 2, 200, 4000, **appSettings)
