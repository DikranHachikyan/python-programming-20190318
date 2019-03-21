#!/home/wizard/anaconda3/bin/python

def main():
    app = {
          'title'  :'Text Editor'
        , 'version':'1.3'
        , 'path'   :'/usr/local/'
        , 'proc'   : 10
    }    

    for item in app.items():
        key, value = item
        print(f'{key}==>{value}')
        

main()