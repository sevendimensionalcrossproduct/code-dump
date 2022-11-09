from tkinter import *

#Menu
menu = {'coffee': 15, 'tea':7,'cheese toast':25,'water':5}

#Functions
def choice1():
    item = input("enter name of item: ")
        
    if item in menu:
        print("the price of ", item, "is", menu[item],'\n')
                
    else:
        print('the item "' + item + '" is not in the menu\n')
        
def choice2():
    try:
        budget = int(input('Enter budget:'))
                
        if budget < 1:
            print('Input must be a positive number\n')
        
        elif budget < min(menu.values()):
            print("No items within budget found\n")
                
        else:
            print("\nItems within budget:\n")
                    
            for ass, sex in menu.items():
                if sex <= budget:
                    print(ass, sex)
                            
            print('')

    except ValueError:
        print('Not an integer\n')

def choice3():
    try:
        name = str(input("Enter new item name: "))
        if name in menu.keys():
            print(name,"is already on the menu\n")
                
        else:
            price = int(input("Enter item price: "))
                
            if price <= 0:
                print("Price must be a positive number\n")
                    
            else:
                menu[name] = price
                print("\nThe updated menu is:\n")
                    
                for cream,pie in menu.items():
                    print(cream,pie)
                print('')
                        
    except ValueError:
        print("Input must be an integer\n")
        
def choice4():
    delete = str(input("Enter item to be deleted from menu: "))
            
    if delete in menu.keys():
        del menu[delete]
        print("\nThe updated menu is:\n")
                
        for left_asscheek,right_asscheek in menu.items():
            print(left_asscheek, right_asscheek)
                    
        print('')
                    
    else:
        print('Entry: "' + str(delete) + '" is not on the menu\n')
    
        
def choice5():
    print('')
    for ass, poop in menu.items():
        print(ass, poop)

    print('')

#GUI properties
ass = Tk()
ass.title('lab6_3')
ass.geometry('800x800')
ass.resizable(True,True)

#GUI components
wrap = LabelFrame(ass, text="Menu")
wrap.grid(row=40,column=40,padx=5,pady=5)


[Label(wrap, text=ass).grid(row=sex,column=0,padx=5,pady=5) for ass,sex in menu.items()]
[Label(wrap, text=(sex,'$')).grid(row=sex,column=2,padx=5,pady=5) for ass,sex in menu.items()]


ass.mainloop()from tkinter import *

#Menu
menu = {'coffee': 15, 'tea':7,'cheese toast':25,'water':5}

#Functions
def choice1():
    item = input("enter name of item: ")
        
    if item in menu:
        print("the price of ", item, "is", menu[item],'\n')
                
    else:
        print('the item "' + item + '" is not in the menu\n')
        
def choice2():
    try:
        budget = int(input('Enter budget:'))
                
        if budget < 1:
            print('Input must be a positive number\n')
        
        elif budget < min(menu.values()):
            print("No items within budget found\n")
                
        else:
            print("\nItems within budget:\n")
                    
            for ass, sex in menu.items():
                if sex <= budget:
                    print(ass, sex)
                            
            print('')

    except ValueError:
        print('Not an integer\n')

def choice3():
    try:
        name = str(input("Enter new item name: "))
        if name in menu.keys():
            print(name,"is already on the menu\n")
                
        else:
            price = int(input("Enter item price: "))
                
            if price <= 0:
                print("Price must be a positive number\n")
                    
            else:
                menu[name] = price
                print("\nThe updated menu is:\n")
                    
                for cream,pie in menu.items():
                    print(cream,pie)
                print('')
                        
    except ValueError:
        print("Input must be an integer\n")
        
def choice4():
    delete = str(input("Enter item to be deleted from menu: "))
            
    if delete in menu.keys():
        del menu[delete]
        print("\nThe updated menu is:\n")
                
        for left_asscheek,right_asscheek in menu.items():
            print(left_asscheek, right_asscheek)
                    
        print('')
                    
    else:
        print('Entry: "' + str(delete) + '" is not on the menu\n')
    
        
def choice5():
    print('')
    for ass, poop in menu.items():
        print(ass, poop)

    print('')

#GUI properties
ass = Tk()
ass.title('lab6_3')
ass.geometry('800x800')
ass.resizable(True,True)

#GUI components
wrap = LabelFrame(ass, text="Menu")
wrap.grid(row=40,column=40,padx=5,pady=5)


[Label(wrap, text=ass).grid(row=sex,column=0,padx=5,pady=5) for ass,sex in menu.items()]
[Label(wrap, text=(sex,'$')).grid(row=sex,column=2,padx=5,pady=5) for ass,sex in menu.items()]


ass.mainloop()