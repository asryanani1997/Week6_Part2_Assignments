#Ex1
def x(name, number):
    if number == 1:
        return "Hello "+ name.capitalize()
    elif number == 0:
        return "Bye "+name.capitalize()

print(x("alon", 1))

#Ex2
def test_jackpot(x, y, z, o):
    if len(set([x, y, z, o])) == 1:
        return True
    if len(set([x, y, z, o]))!=1:
        return False
    
print(test_jackpot("abc", "abc", "abc", "abc"))

#Ex3
def hurdle_jump(hurdle, jumper):
    if max(hurdle)<=jumper:
        return True
    else: 
        return False
    
print(hurdle_jump([1, 2, 1], 1))

#Ex4
def factorize(divident):
    factors=[]
    for i in range(1,divident+1):
        if divident%i==0:
            factors.append(i)

    return factors

print(factorize(12))

#Ex5
def count_palindromes (x, y):
    palindromes=0
    for i in range(x, y+1):
            if str(i)==str(i)[::-1]:
                palindromes+=1

    return palindromes

print(count_palindromes(878, 898))