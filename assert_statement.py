def divisors(num):
    assert num > 0, "Must ingresar numero positivo "
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors




def run():
    num =  input('Enter a number :  ')
    assert num.isnumeric(), "Must to enter a number "
    print(divisors(int(num)))
    print("Program End")
    
       

if __name__ == '__main__':
    run()