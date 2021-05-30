def fizz():
    for x in range(1,100):
        output = ""
        if(x % 3 == 0 and x % 5 == 0):
            output + ("FizzBuzz")
        elif(x % 5 == 0):
            output + ("Buzz")
        elif(x % 3 == 0):
            output + ("Fizz")
        else:
            output + str(x)
    return output
       




