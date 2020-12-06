#database.py
import shelve, sys

def store_person(db):
    """
    Query user for data and store it in the shelf object
    """
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = int(input('Enter age: '))
    person['phone'] = input('Enter phone number: ')

    db[pid] = person

def lookup_person(db):
    """
    Query user for ID and desired field and fetch the corresponding data from the shelf object
    """
    
    pid = input('Enter unique ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print('Available commands are: ')
    print('store : Stores information about a person')
    print('lookup : Looks p a person from ID number')
    print('quit : save changes and exit')
    print('? : prints the message')

def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('/home/mikolaj/PythonVSC/Lie/database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__== '__main__': main()