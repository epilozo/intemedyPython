def divisors(num):
    try:
        if num < 0:
            raise ValueError("You have to enter a positive number ")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors

    except ValueError as ve:
        print(ve)
        return []


def run():
    try:
        num = int(input('Enter a number :  '))
        print(divisors(num))
        print("Program End")
    except ValueError:
        print("You have to enter a number ")
  
       

if __name__ == '__main__':
    run()