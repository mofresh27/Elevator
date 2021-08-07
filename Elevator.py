def Elevator():
    try:
        floor = int(input("Floor Number\n"))
        if floor == 1:
            print('Welcome to the first floor')
            Elevator()
        elif floor == 2:
            print('welcome to the second floor')
            Elevator()
        elif floor ==3:
            print('welcome to the third floor')
            Elevator()
        elif floor ==4:
            print('welcome to the fourth floor')
            Elevator()
        elif floor == 5:
            print('welcome to the fith floor')
            Elevator()
        elif floor ==6:
            print('welcome to the sixth floor')
            Elevator()
        elif floor ==7:
            print('welcome to the seventh floor')
            Elevator()
        else:
            floor < 7
            print ("We have not completed that floor just yet")
            Elevator()
    except ValueError:
        print("invalid choice")
        Elevator()




Elevator()


