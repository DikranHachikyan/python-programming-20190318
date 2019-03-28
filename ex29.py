#!/home/wizard/anaconda3/bin/python

def show(title, *args, **kwargs):
    print(f'Title:{title}')

    print('Args:')
    for v in args:
        print(f'arg:{v}')

    if 'path' in kwargs:
        print(f"path :{kwargs['path']}")

    if 'log' in kwargs:
        print(f"log file:{kwargs['log']}")    

if __name__ == '__main__':
    show('Text Editor')

    show('Text Editor', 1, 2, 200, 4000)

    show('Text Editor', 1, 2, 200, 4000, path='/usr/bin',log='/var/log/app.log')
    
    appSettings = {
          'path':'/usr/local/bin'
        , 'log':'/var/log/editor.log'
        , 'mem': 4096
    }

    show('Text Editor', 1, 2, 200, 4000, **appSettings)
