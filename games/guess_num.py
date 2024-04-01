num=27
guess=7

print("Total  number of attempts left :",guess)
while(guess!=0):
    num1=int(input("Enter your guess: less then 100: "))

    if(num1==num):
        print("Congrats! Your guess is correct!")
        input()
        break
    else:
        guess-=1
        print("Your remaining guess: ",guess)
        if(guess==0):
            print("GAME OVER!!!")
            input()
        elif(num1-5>num):
            print("Your guess is too high! ")
        elif(num1+5<num):
            print("Your guess is too low!")
        else:
            if(num-num1<=5 and num-num1>0 ):
               print("Your guess is too close try increasing!")
            else:
                print("Your guess is still abit far! try decreasing")
        continue