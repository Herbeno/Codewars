# Este problema pede para que façamos um código que multiplique um número por 8 se ele for par ou por nove se ele for impar.
def simple_multiplication(number) :
# Teremos que usar o 'if' que significa uma condição para que o algoritmo realize alguma operação, e também usará o '%' que é a operação que retorna o resto da divisão.
    if number % 2 == 0:
        simple_multiplication = number * 8
        return simple_multiplication
    # No código acima, colocamos uma codição de que se o resto da divisão do 'number' por 2 for igual a 0(ou seja, o número é par), ele será multiplicado por 8.
    # Logo, a próxima possibilidade que teremos é de números ímpares, que foram os que restaram, e seram multiplicados por 9.
    simple_multiplication = number * 9
    return simple_multiplication
