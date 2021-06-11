import random
import os

clear = lambda: os.system('cls') 

def print_screen(word, guess, errors):
    clear()
    print('Vidas: ' + str(5 - errors))
    print("\n")
    print("Adivina la Palabra!")
    print(guess.upper())
    print("\n")

    try: # con el try se permite continuar jugando despues de un error
        letra = input("Ingresa una letra: ")
        assert letra.isalpha(), input('Ups! esto no es una letra, Preciona enter para continuar')
        assert len(letra) == 1, input('Ingresa solo una letra! Preciona enter para continuar')
    except AssertionError:
        print(AssertionError)

    for i, char in enumerate(word):
        if letra == char:
            guess = guess[:i] + letra + guess[i+1:]

    return guess

def run():
    with open("./archivos/datos.txt", "r", encoding="utf-8") as data:
        words = [word.replace("\n", "") for word in data]

    choosed_word = random.choice(words)
    guess_word = ''
    errors = 0
    for i in choosed_word:
        guess_word += '-'

    while (guess_word != choosed_word and errors < 5):
        previous = guess_word
        guess_word = print_screen(choosed_word, guess_word, errors)
        if previous == guess_word:
            errors += 1
    
    clear()
    if guess_word == choosed_word:
        print("Felicidades Ganaste!")
        print("La palabra era: " + choosed_word.upper())
    else: 
        print("Lo siento, perdiste :(")
        print("La palabra era: " + choosed_word.upper())
    


if __name__ == '__main__':
    run()