###On our honor, as CCSF students, we Ashlan Finn and Jennifer Garcia have neither given or received inappropriate help with this assignment.
###

#Step 1:We will import all of the background information we need for our program to function
#Step2:Create variables which will be called throughout the program
#Step3:Make loop function that keeps track of how many times the user has played \
#Step3pt2:and taliors response accordingly
#Step4:Call functions from HWfxns to use in the loop

import turtle
import time
import sys
import HW3fxns
#variables which we will call later in the program
PosNum = ("12","1","2","3","4","5","6","7","8","9","10","11") #numbers that will be printed out 
NegNum = ("-12","-11","-10","-9","-8","-7","-6","-5","-4","-3","-2","-1") #numbers that will be printed out
time_params = list(time.localtime())
NumTr = 0
radius = 200
'''
Chat text which will be called throughout the program
'''
ChaText = ["Hello and welcome to our program  that uses clocks Yay! Do you want to take part in our program? Y or N. ",\
           "Once more [Y/N]", "Do you see your world as negative or positive [-/+]? ","How do you rate your world this time, plus or minus [+/-]? ",\
           "The time is now. Your reaction to that bracing thought? ", "The time is still now. Your reaction? ", "How will you change the time? in HH:MM format "]  


while True:

    #If this is the first time playing responses will be taliored
    if NumTr == 0:
        userinput = input(ChaText[0])
        #validating inputs
        Error = HW3fxns.validate_text(userinput, "YN", False)
        if Error == False:
            print("Your answer was not a valid response")
            continue
    else:
        userinput = input(ChaText[1])
        Error = HW3fxns.validate_text(userinput, "YN", False)
        if Error == False:
            print("Your answer was not a valid response")
            continue
    if userinput == "N":
        raise SystemExit(0)
    else:
        NumTr += 1
    #using 1 to determine if this is the first playthrough to determine text   
    if NumTr <= 1:    
        PNans = input(ChaText[2])
        Error = HW3fxns.validate_text(PNans, "+/-", False)
        #Validating the + or -
        if Error == False:
            print("Your answer was not a valid response")
            continue
        #Positive clock first time around
        if PNans == '+':
            (joe,canvas) = HW3fxns.turtle_init("black", "red", 3, 0, "classic" )
            ruth = joe.clone()
            respon = input(ChaText[4])
            HW3fxns.draw_clock(joe, radius+100, '+' , respon)
            HW3fxns.clock_hands(ruth, time_params, 0,0, radius  )            
            HHMM = input(ChaText[6]).split(':')
            if len(HHMM) != 2:
                print(str(HHMM) + " is not two ints seperated by ':' please try again")
                continue
            NewHours = HW3fxns.convert_validate_int(HHMM[0])
            NewMinutes = HW3fxns.convert_validate_int(HHMM[1])
            if NewHours == None or NewMinutes == None:
                print(str(NewHours)+" "+ str(NewMinutes) + ' is not a valid response, try again')
                continue
            (joe,canvas) = HW3fxns.turtle_init("red", "black", 3, 0, "classic" )
            HW3fxns.draw_clock(joe, radius+100, '+' , respon)
            HW3fxns.clock_hands(joe, time_params, NewHours,NewMinutes, radius  )

            continue
        
        #negative clock first time around
        elif PNans == '-':
            (joe,canvas) = HW3fxns.turtle_init("green", "Black", 3, 0, "classic" )
            ruth = joe.clone()
            respon = input(ChaText[4])
            HW3fxns.draw_clock(joe,radius+ 100, '-' , respon)
            HW3fxns.clock_hands(ruth, time_params, 0,0, radius  )
            HHMM = input(ChaText[6]).split(':')
            if len(HHMM) != 2:
                print(str(HHMM) + " is not two ints seperated by ':' please try again")
                continue
            NewHours = HW3fxns.convert_validate_int(HHMM[0])
            NewMinutes = HW3fxns.convert_validate_int(HHMM[1])
            if NewHours == None or NewMinutes == None:
                print(str(NewHours)+" "+ str(NewMinutes) + ' is not a valid response, try again')
                continue
            (joe,canvas) = HW3fxns.turtle_init("green", "black", 3, 0, "classic" )
            HW3fxns.draw_clock(joe,radius+ 100, '-' , respon)
            HW3fxns.clock_hands(joe, time_params, NewHours,NewMinutes, radius  )
            continue
    #If this isn't the first time playing then different text appears
    else:
        PNans = input(ChaText[3])
        Error = HW3fxns.validate_text(PNans, "+/-", False)
        #Validating the + or -
        if Error == False:
            print("Your answer was not a valid response")
            continue
        #positive clock second or more times around
        if PNans == '+':
            (joe,canvas) = HW3fxns.turtle_init("green", "Black", 3, 0, "classic" )
            ruth = joe.clone()
            respon = input(ChaText[5])
            HW3fxns.draw_clock(joe,radius+ 100, '+' , respon)
            HW3fxns.clock_hands(ruth, time_params, 0,0, radius  )
            HHMM = input(ChaText[6]).split(':')
            if len(HHMM) != 2:
                print(str(HHMM) + " is not two ints seperated by ':' please try again")
                continue
            NewHours = HW3fxns.convert_validate_int(HHMM[0])
            NewMinutes = HW3fxns.convert_validate_int(HHMM[1])
            if NewHours == None or NewMinutes == None:
                print(str(NewHours)+" "+ str(NewMinutes) + ' is not a valid response, try again')
                continue
            (joe,canvas) = HW3fxns.turtle_init("green", "black", 3, 0, "classic" )
            HW3fxns.draw_clock(joe,radius+ 100, '+' , respon)
            HW3fxns.clock_hands(joe, time_params, NewHours,NewMinutes, radius  )
            continue

        #negative clock second or more times around
        elif PNans == '-':
            (joe,canvas) = HW3fxns.turtle_init("green", "Black", 3, 0, "classic" )
            ruth = joe.clone()
            respon = input(ChaText[5])
            HW3fxns.draw_clock(joe,radius+ 100, '-' , respon)
            HW3fxns.clock_hands(ruth, time_params, 0,0, radius  )
            HHMM = input(ChaText[6]).split(':')
            if len(HHMM) != 2:
                print(str(HHMM) + " is not two ints seperated by ':' please try again")
                continue
            NewHours = HW3fxns.convert_validate_int(HHMM[0])
            NewMinutes = HW3fxns.convert_validate_int(HHMM[1])
            if NewHours == None or NewMinutes == None:
                print(str(NewHours)+" "+ str(NewMinutes) + ' is not a valid response, try again')
                continue
            (joe,canvas) = HW3fxns.turtle_init("green", "black", 3, 0, "classic" )
            HW3fxns.draw_clock(joe,radius+ 100, '-' , respon)
            HW3fxns.clock_hands(joe, time_params, NewHours,NewMinutes, radius  )
            continue
    '''
    '''


### Test Reports

###Test 1:
#===================== RESTART: D:\HW3\Homework_3_grwk.py =====================
#Hello and welcome to our program  that uses clocks Yay! Do you want to take part in our program? Y or N. Y
#How do you rate your world this time, plus or minus [+/-]? +
#The time is still now. Your reaction? asdf
#(10.883333333333333, 53)
#Traceback (most recent call last):
#  File "D:\HW3\Homework_3_grwk.py", line 113, in <module>
#    HHMM = input(ChaText[7]).split(':')
#IndexError: list index out of range
#>>>

### Comments: Minor fixing with signs



###Test 2:
#===================== RESTART: D:\HW3\Homework_3_grwk.py =====================
#Hello and welcome to our program  that uses clocks Yay! Do you want to take part in our program? Y or N. N
#>>>

###Comments:Works as planned


###Test 3:
#===================== RESTART: D:\HW3\Homework_3_grwk.py =====================
#Hello and welcome to our program  that uses clocks Yay! Do you want to take part in our program? Y or N. Y
#Do you see your world as negative or positive [-/+]? +
#The time is now. Your reaction to that bracing thought? Sfds
#(10.916666666666668, 55)
#How will you change the time? in HH:MM format 5:40
#(4.583333333333332, 35)
#Once more [Y/N]Y
#How do you rate your world this time, plus or minus [+/-]? -
#The time is still now. Your reaction? SFddf
#(10.916666666666668, 55)
#Traceback (most recent call last):
#  File "D:\HW3\Homework_3_grwk.py", line 134, in <module>
#    HHMM = list(input(ChaText[7]).split(':'))
#IndexError: list index out of range
#>>>
