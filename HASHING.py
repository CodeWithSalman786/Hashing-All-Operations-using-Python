# AUTHOR: @CodeWithSalman
# CREATING HASH TABLE USING THE CONCEPT OF DICTIONARY.
hash_Table = {}
def inserting():
    key = str(input("Enter the Key: "))
    value = str(input("Enter the Value for key Now: "))
    hash_Table[key] = value
def access():
    key = str(input("Enter the Key: "))
    try:
        result = hash_Table[key]
        print(result)
    except:
        print(hash_Table.get(key, "No such key found."))
        print("Key Status: ", key in hash_Table)
def update():
    key = str(input("Enter the Key: "))
    value = str(input("Enter the Value for key Now: "))
    hash_Table[key] = value
def delete():
    key = str(input("Enter the Key: "))
    del hash_Table[key]
def key_Status():
    key = str(input("Enter the Key: "))
    print(hash_Table.get(key, "No such key found."))
    print(key in hash_Table)
def printing_Keys():
    for keys in hash_Table:
        print(keys)
def keys_Values():
    for keys, values in hash_Table.items():
        print(f'{keys}: {values}')
def size():
    print(len(hash_Table))
def display():
    print(hash_Table)
def copy():
    copytable = hash_Table.copy()
    print(copytable)
def clearing():
    hash_Table.clear()
    print(hash_Table)
if __name__ == '__main__':
    while True:
        print("1 = Inserting Key")
        print("2 = Accessing Key")
        print("3 = Updating Key")
        print("4 = Deleting Key")
        print("5 = Checking Key Status")
        print("6 = Printing Keys")
        print("7 = Printing Keys and Values")
        print("8 = Size of Hash Table")
        print("9 = Copy Hash Table")
        print("10 = Printing Hash Table")
        print("11 = Clear Hash Table")
        # NOW LET'S GET INPUT FORM USER.
        selection = int(input("Make any One Selection from Above: "))
        if selection == 1:
            # USE OF INSERT FUNCTION.
            inserting()
        elif selection == 2:
            # ACCESSING SPECIAL KEY VALUE.
            access()
        elif selection == 3:
            # UPDATING KEY VALUE.
            update()
        elif selection == 4:
            # DELETING KEY VALUE.
            delete()
        elif selection == 5:
            # CHECKING KEY STATUS.
            key_Status()
        elif selection == 6:
            # PRINTING ALL KEYS VALUE.
            printing_Keys()
        elif selection == 7:
            # PRINTING KEYS VALUE AND THEIR DATA.
            keys_Values()
        elif selection == 8:
            # PRINTING SIZE OF HASH TABLE.
            size()
        elif selection == 9:
            # CREATING COPY OF HASH TABLE.
            copy()
        elif selection == 10:
            # DISPLAYING ALL THE DATA IN THE HASH TABLE.
            display()
        elif selection == 11:
            # CLEARING ALL THE DATA IN THE HASH TABLE.
            clearing()
        else:
            print("Invalid Input or Input out of Range!")
