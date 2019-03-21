#!/home/wizard/anaconda3/bin/python

def main():
    users = ['anna','maria','john', 'mary']
    mails = ['anna@no.com','maria@no.com','john@no.com','none']

    for data in zip(users,mails):
        name, mail = data
        print(f'{name} ==> {mail}')    

main()