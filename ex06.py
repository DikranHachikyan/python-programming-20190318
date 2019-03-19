#!/home/wizard/anaconda3/bin/python

def newFile():
    print('Create a new file')

def openFile():
    print('Open file ...')

def saveFile():
    print('Save file')

def quitApp():
    print('Quit')

def main():
    action = {
        'n' :newFile
        ,'o':openFile
        ,'s':saveFile
        ,'q':quitApp
    }

    ch = input('Enter n-new, o-open, s-save, q-quit:')

    if ch in action:
        action[ch]()
    else:
        print('Invalid option:{}'.format(ch))

main()