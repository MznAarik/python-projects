#***** Health Management System *****#
# three clients ram, sita, shyam

#retrieving time stamp
def get_date():
    import datetime
    return datetime.datetime.now()

print("Enter 1:Ram 2:Sita 3:Shyam")
client_name = int(input())
print("Press 1:Diet 2:Exercise")
client_data = int(input())
print("Press 1: log an entry! 2: retrieve your data!")
client_choice = int(input())
# for ram
if (client_name == 1):
    # for diet
    if (client_data == 1):
        # to record the entry
        if client_choice == 1:
            with open ("ramD.txt", "a") as f:
                print("What did you have for your diet?")
                ram_diet = str(input())
                f.write(ram_diet + " : [" + str(get_date()) + "]\n")
                f.close()
                print("Your diet is been successfully recorded!")
                input()
        # to retrieve the record
        elif client_choice == 2:
            with open("ramD.txt", "r") as f:
                print("________Your recent diet________ \n")
                print(f.read())
                f.close()
                input()
        else:
            print("ERROR! Enter your correct choice!!")
            input()
    # for exercise
    elif (client_data == 2):
        if (client_choice == 1):
            with open ("ramE.txt" , "a") as f:
                print("What did you have for your diet?")
                ram_exer = str(input())
                f.write(ram_exer + " : [" + str(get_date()) + "]\n")
                f.close()
                print("Your diet is been successfully recorded!")
                input()
        elif(client_choice == 2):
            with open ("ramE.txt", "r") as f:
                print("________Your recent exercise________ \n")

                print(f.read())
                f.close()
                input()
        else:
            print("ERROR! Enter correct choice!!")
            input()
    else:
        print("Press correct input!!")
        input()
# for sita
elif (client_name == 2):
    # for diet
    if (client_data == 1):
        if (client_choice == 1):
            with open("sitaD.txt", "a") as f:
                print("What did you have for your diet?")
                sita_diet = str(input())
                f.write(sita_diet + " : [" + str(get_date().date()) + "]\n")
                f.close()
                print("Your diet is been successfully recorded!")
                input()
        elif(client_choice == 2):
            with open ("sitaE.txt", "a") as f:
                print("________Your recent diet________ \n")
                print(f.read())
                f.close()
        else:
            print("ERROR! Enter correct choice!")
            input()          
    #for exercise
    elif(client_data == 2):
        if(client_choice == 1):
            with open("sitaE.txt", "a") as f:
                print("What exercise did you perform?")
                sita_exer = str(input())
                f.write(sita_exer + "[" + str(get_date()) + "]" + "\n")
                f.close()
                print("Your exercise is been successfully recorded")
                input()
        elif(client_choice == 2):
            with open("sitaE.txt") as f:
                print("________Your recent exercise________ \n")
                print(f.read())
                f.close()
        else:
            print("ERROR! Please enter correct choice!!")
            input()
    else:
        print("Press correct input!!")
        input()
# for shyam
elif (client_name == 3):
    #for diet
    if (client_data == 1):
        if (client_choice == 1):
            with open ("shyamD.txt" , "a") as f:
                print("What did you have for your diet?")
                shyam_diet= str(input())
                f.write(shyam_diet + "[" + str(get_date()) +"]" + "\n")
                f.close()
                print("Your diet is been recorded successfully!")
                input()
        elif(client_choice == 2):
            with open ("shyamD.txt", "r") as f:
                print("________Your recent diet________ \n")
                print(f.read())
                f.close()
    #for exercise
    elif(client_data == 2):
        if (client_choice == 1):
            with open("shyamE.txt", "a") as f:
                print("What exercise did you perform?")
                shyam_exer = str(input())
                f.write(shyam_exer + "[" + str(get_date()) +"]" + "\n")
                print("Your exercise is been recorded successfully!")
                input()
                f.close()
        elif (client_choice == 2):
            with open ("shyamE.txt", "r") as f:
                print("________Your recent exercise________ \n")
                print(f.read())
                f.close()
                input()
        else:
            print("Error! Enter correct choice!")
            input()
    else:
        print("Press correct input!!")
        input()
# if user inputs more than 3
else:
    print("Invalid Client!!")
    input()
        