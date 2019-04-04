#!/home/wizard/anaconda3/bin/python

def sort10(el):
    return (el[1],el[0])

if __name__ == '__main__':
    f = lambda x: x**2 if x % 2 else x**3

    print('result 1:', f(4))
    print('result 2:', f(5))

    items = [('A', 5, 7), ('Z', 2, 6), ('B', 4, 6), ('D', 2, 5)]
    #items.sort()
    #print('in place sorted:',items)
    
    #items.sort(key=lambda el:(el[1]))
    #print('2el:',items)

    #items.sort(key=lambda el:(el[1],el[0]))
    #print('2el then 1el:', items)
    
    items.sort(key=sort10)
    print('2el then 1el:', items)

    nums = [1,2,3,4,5]

    for x in map(lambda el: el**2, nums):
        print('x:', x)

    ls = list( map(lambda el: el**2, nums))
    print('ls:',ls)