#!/home/wizard/anaconda3/bin/python

def quarters(next_quarter=0.0):
    while True:
        newValue = (yield next_quarter)
        if newValue is not None:
            next_quarter = newValue
            continue
        next_quarter += 0.25

if __name__ == '__main__':
    result = []
    gnr = quarters()
    while len(result) < 7:
        v = next(gnr)
        if v == 1:
            gnr.send(10)
        result.append(v)

    print(result)
    