# Este problema pede para que façamos um código que multiplique um número por 8 se ele for par ou por nove se ele for impar.
def simple_multiplication(number) :
    if number % 2 == 0:
        simple_multiplication = number * 8
        return simple_multiplication
    else:
        return number * 9