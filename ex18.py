#!/home/wizard/anaconda3/bin/python

def main():
    array = [10,5,2,12,7,1]
    value = 8
    found = False
    hashTable = {}

    for item in array:
        s = value - item
        if s in hashTable:
            found = True
            break
        hashTable[item] = True

    out = f'result: {value} = {item} + {s}' if found else 'Not Found'
    print(hashTable)
    print(out)
    print(f'{array} Value:{value}')
    



main()