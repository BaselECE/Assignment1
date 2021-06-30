number1 =eval (input ("enter the first number : "))
number2 =eval (input ("enter the second number : "))
process =input ("enter the process(*,/,+,-):") # ask user to type process
# test what process to do
if (process=='*') :                             
    print (number1*number2)
elif (process=='/') :
    print (number1/number2)
elif (process=='+') :
    print(number1+number2)
else :
    print(number1-number2)

    
