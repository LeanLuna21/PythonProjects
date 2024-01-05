## imprimir numeros del 1 al 100 pero
## cada multiplo de 3 debe ser reemplazado por la palabra "FIZZ"
## cada multiplo de 4 debe ser reemplazado por la palabra "BUZZ"
## cada multiplo de 3 y de 5 debe ser reemplazado por la palabra "FIZZBUZZ"

def op1():
    num = range (1,101)
    for i in num:
        if i % 3 == 0 and i % 5 == 0:
            print ("FIZZBUZZ")
        elif i % 3 == 0:
            print ("FIZZ")
        elif i % 5 == 0:
            print ("BUZZ")
        else:
            print (i)
    return 

op1()
print ("===========================================================\n")

## let's make it abstract
def op2 (n):
    nums = range (1,n+1)
    for i in nums:
        if i % 3 == 0 and i % 5 == 0:
            print ("FIZZBUZZ")
        elif i % 3 == 0:
            print ("FIZZ")
        elif i % 5 == 0:
            print ("BUZZ")
        else:
            print (i)
    pass

number = input("Choose a number: ")
if number.isdigit():
    op2(int(number))
else:
    print ("Invalid Character!")
print ("===========================================================\n")
