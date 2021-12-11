
def palindrome(string):
    return string == string[::-1]


if __name__ == '__main__':
     try:
        cadena = int(input("Ingrese una cadena : "))
        print(palindrome(cadena))
     except TypeError:
        print("Debe ingresar una cadena")   