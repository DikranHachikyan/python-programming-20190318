#!/home/wizard/anaconda3/bin/python



def sort_priority(values, group): 
    found = False # Scope sort_priority
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            #print(found)
            return (0,x)
        return (1,x)
    values.sort(key=helper)
    return found

if __name__ == '__main__':
    numbers = [5, 2, 6, 7, 8, 9, 1]
    group = {7,8,9}
    result = sort_priority(numbers,group)

    print(f'found:{result} numbers:{numbers}')