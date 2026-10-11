#InventoryManagementSystem.py

#InvestoryMenu
def menu():
    print("="*50)
    print("\tNVESTORY MANAGEMENT SYSTEM")
    print("="*50)
    print("\t1. Additems")
    print("\t2. Deleteitems")
    print("\t3. Uodateitems")
    print("\t4. DisplayM(pid)")
    print("\t5. displayitems")
    print("\t6. Exit")
    print("="*50)


#InventoryOperations
from InvestoryExcept import InvalidPIDError,InvalidItemNameError,DuplicatePIDError,ItemNotFoundError,InvalidPriceError
items=[] #golobal Variable
def additems():
    pid=int(input("Enter Product PID: "))
    name=input("Enter Item Name:")
    price=float(input("Enter Item Price:"))
    if(pid<=0):
        raise InvalidPIDError("PID Must Be +VE")
    if (name=="" or name.isdigit()):
        raise InvalidItemNameError("Invalid Item Name")
    if(price<=0):
        raise InvalidPriceError("Price Must Be +VE NUMBERS")
    for data in items:
        if(data[0]==pid):
            raise DuplicatePIDError("PID Already Exists")
    items.append([pid,name,price])
    print("--->Item Successfully Added")
def deleteitems():
    pid=int(input("Enter Product PID:"))
    for data in items:
        if(data[0]==pid):
            items.remove(data)
            print("--->Item Successfully Deleted")
            break
    else:
        raise ItemNotFoundError
def updateitems():
    pid=int(input("Enter Product PID:"))
    name=input("Enter Item Name:")
    price=float(input("Enter New Item Price:"))
    for data in items:
        if(data[0]==pid and data[1]==name):
            if(price<=0):
                raise InvalidPriceError("Price Must Be Positive")
            data[2]=price
            print("--->Item Successfully Updated")
            break
    else:
        raise ItemNotFoundError
def displayitem():
    pid=int(input("Enter Product PID: "))
    for item in items:
        if item[0]==pid:
            print("PID\t\tPName\t\tPrice")
            print(
                "{0}\t\t{1}\t\t{2}".format(item[0],item[1],item[2]))
            break
    else:
        raise ItemNotFoundError
def displayitems():
    print("\nTotal Items In Inventory")
    print("-"*50)
    print("PID\t\tPName\t\tPrice")
    print("-"*50)
    for item in items:
        print("{0}\t\t{1}\t\t{2}".format(item[0], item[1], item[2]))
    print("-"*50)


#InventoryOperationsMainProgram
from InvestoryExcept import InvalidPIDError, InvalidItemNameError, InvalidPriceError, ItemNotFoundError,DuplicatePIDError
from InvestoryMenu import menu
from InventoryOperations import additems,deleteitems,updateitems,displayitem,displayitems
while True:
    try:
        menu()
        ch=int(input("Enter Choice:"))
        match ch:
            case 1:
                try:
                    additems()
                except ValueError:
                    print("\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")
                except InvalidPIDError:
                    print("\tDONT ENTER ZERO AND -VE NUMBER  PLEACE TRY--AGAIGN")
                except InvalidItemNameError:
                    print("\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")
                except InvalidPriceError:
                    print("\tDONT ENTER ZERO AND -VE NUMBER  PLEACE TRY--AGAIGN")
                except DuplicatePIDError:
                    print("\tDONT ENTER ZERO AND -VE NUMBER AND DUPLICATEVALUE  PLEACE TRY--AGAIGN")
            case 2:
                try:
                    deleteitems()
                except ValueError:
                    print("\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")

                except ItemNotFoundError:
                    print("\tTHIS PRODUCT ID IS NOT AVAILABLE FOR CHOICE -- TRY AGAIN")
            case 3:
                try:
                    updateitems()
                except ValueError:
                    print("\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")
                except InvalidPriceError:
                    print("\tDONT ENTER ZERO AND -VE NUMBER  PLEACE TRY--AGAIGN")
                except ItemNotFoundError:
                    print("\tTHIS PRODUCT ID IS NOT AVAILABLE FOR CHOICE -- TRY AGAIN")
            case 4:
                try:
                    displayitem()
                except ValueError:
                    print("\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")
                except ItemNotFoundError:
                    print("\tTHIS PRODUCT ID IS NOT AVAILABLE FOR CHOICE -- TRY AGAIN")
            case 5:
                try:
                    displayitems()
                except Exception:
                    print("\tDisplay Items Error")
            case 6:
                print(
                    "\tThank You for using Inventory Management System")
                print("\tVisit Again")
                break
            case _:
                print("\tDONT ENTER ZERO AND -VE NUMBER  PLEACE TRY--AGAIGN")
    except ValueError:
        print(
            "\tDON'T ENTER ALNUMS/STRS/SYMBOLS "
            "FOR CHOICE -- TRY AGAIN")