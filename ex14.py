#!/home/wizard/anaconda3/bin/python

def main():
    tpl = 11,22,33,44,55

    for key, value in enumerate(tpl, 2):
        print(f'key={key} value={value}')

main()