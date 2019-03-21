#!/home/wizard/anaconda3/bin/python

def main():
    app = {
          'title'  :'Text Editor'
        , 'version':'1.3'
        , 'path'   :'/usr/local/'
        , 'proc'   : 10
    }    

    for idx, key in enumerate(app):
        print(f'idx={idx} key={key}')
        

main()