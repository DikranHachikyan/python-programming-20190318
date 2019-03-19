#!/home/wizard/anaconda3/bin/python

def main():
    x = int(input('x='))

    # (x > 0)? true_part:false_part
    # true_part if x > 0 else false_part
    m = x if x > 0 else 10
    print('m =',m)

main()