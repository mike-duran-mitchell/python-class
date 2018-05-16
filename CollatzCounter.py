#rileywestonmiller@outlook.com
#practical programming, third edition by Gries, Campbell & Montojo
#expert python programming - second edition

def isEven(num):
    return num%2==0
    
def Collatz(num):
    count=0
    while num!=1:
        count=1+count
        if isEven(num):
            num=num/2
        else:
            num=num*3+1
    return count

def CollatzCount(numbersToRun):   
    previousCount=0
    counter=0
    while counter < numbersToRun:
        counter+=1
        if Collatz(counter)>previousCount:
            previousCount=Collatz(counter)
            winningNumber=counter
    print(previousCount,winningNumber)

CollatzCount(35000)