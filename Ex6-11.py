#Ex6 

def vowel(v):
    vowels="aoiue"
    return(v) in vowels

def split(x): 
    vowels = []
    consonants = []
    for i in x: 
        if vowel(i):
            vowels.append(i)
        else:
            consonants.append(i)
    
    return "".join(vowels) + "".join(consonants)

print(split("What's the time?"))

#Ex7 
def hacker_speak (x):
    final=""
    for i in x:
        if i=="a":
            final+= "4"
        elif i=="e":
            final+= "3"
        elif i=="i":
            final+= "1"
        elif i=="o":
            final+= "0"
        elif i=="s":
            final+= "5"
        else: 
            final+=i
    return final
print(hacker_speak("javascript is cool"))

#Ex8
def return_end_of_number (x):
    if x%10==1:
        return str(x)+"-st"
    if x%10==2:
        return str(x)+"-nd"
    if x%10==3:
        return str(x)+"-rd"
    else:
        return str(x)+"-th"
    
print(return_end_of_number(34))

#Ex9

def convert(x):
    if x[-2:]=="*C":
        Celsius = float(x[:-2])
        Fahrenheit=(round(Celsius * 9/5 + 32))
        return f"{Fahrenheit}*F"
    elif x[-2:]=="*F":
        Fahrenheit =float(x[:-2])
        Celsius=(round(Fahrenheit-32)*5/9)
        return f"{Celsius}*C"
    else:
        return "Error"
print(convert("33"))
    
#Ex10
def reversed_complement(x):
    final=""
    for i in reversed(x):
        if i=="A":
            final+= "U"
        elif i=="U":
            final+= "A"
        elif i=="G":
            final+= "C"
        elif i=="C":
            final+= "G"
    return final 
print(reversed_complement("UCUCG"))

#Ex11
def arithmetic_operation(x):
    divided=x.split()
    num1=int(divided[0])
    operator=divided[1]
    num2=int(divided[2])
    if operator=="+":
         return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="//":    
        if num2==0:
            return -1
        else:
            return num1//num2
    
    
print(arithmetic_operation("12 // 0"))