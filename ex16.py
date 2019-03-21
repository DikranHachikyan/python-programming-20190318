#!/home/wizard/anaconda3/bin/python

def main():
    app = {
          'title'  :'Text Editor'
        , 'version':'1.3'
        , 'path'   :'/usr/local/'
        , 'proc'   : 10
    }    

    for key in app:
        print(f'key={key} value={app[key]}')
        

main()