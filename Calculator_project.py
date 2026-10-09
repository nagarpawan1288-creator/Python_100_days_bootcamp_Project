logo = r"""
  _____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
"""
print(logo)
def add(n1,n2):
    result = n1+n2
    return result

def sub(n1,n2):
    result = n1-n2
    return result

def mult(n1,n2):
    result = n1*n2
    return result

def div(n1,n2):
    result = n1/n2
    return result



calc = {"+":add,"*":mult,"-":sub,"/":div}

def calculator():    
    f_num = float(input("Enter your first number\n"))
    should_continue = True
    while should_continue:
        for x in calc:
            print(x)

        opertaion = input("Enter a operation which is showing above\n")

        sec_num = float(input("Enter your second number\n"))

        answer = calc[opertaion](f_num,sec_num)
        print(f"{f_num} {opertaion} {sec_num} = {answer}")

        choice = input(f"If you want continue calculation with {answer} type 'y' or type 'n' for restart\n")

        if choice == "y":
            f_num = answer
            
        elif choice == "n":
            should_continue= False
            calculator()
        else:
            print("You entered invalid input try again")
            should_continue = False


calculator()






