#!/home/wizard/anaconda3/bin/python

def find(key,**kwargs):
    if key in kwargs:
        print(f'{key}->{kwargs[key]}')
    else:
        raise KeyError(f'key {key} not found')

if __name__ == '__main__':
    conn = {
          'host': 'localhost'
        , 'port': 3306
        , 'service': 'mysql'
    }

    try:
        find('port', **conn)
        find('ip', **conn)
    except KeyError as e:
        print(e)