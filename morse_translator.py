#  * Re::  CÓDIGO MORSE
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#  * - Debe detectar au:máticamente de qué tipo se trata y realizar la conversión.
#  * - En morse se soporta raya "—", pun: ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#  * - El alfabe: morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
#  *
##      Solución:
## 1- el programa debera detectar que tipo de tex: se introduce (natural o morse)
## 2- dos caminos:
##      a- texto natural -> convertir a morse
##      b- codigo morse -> convertir a natural
## 3- si el usuario llegase a ingresar alguna otra opcion, quedara descartada

import string
morse_dict = {
    "A" : ".-", "N" : "-.", "0" : "-----",
    "B" : "-...", "Ñ" : "--.--", "1" : ".----",
    "C" : "-.-.", "O" : "---", "2" : "..---",
    "CH" : "----", "P" : ".--.", "3" : "...--",
    "D" : "-..", "Q" : "--.-", "4" : "....-",
    "E" : ".", "R" : ".-.", "5" : ".....",
    "F" : "..—.", "S" : "...", "6" : "-....",
    "G" : "--.", "T" : "-", "7" : "--...",
    "H" : "....", "U" : "..-", "8" : "---..",
    "I" : "..", "V" : "...-", "9" : "----.",
    "J" : ".---", "W" : ".--", "." : ".-.-.-",
    "K" : "-.-", "X" : "-..-", "," : "--..--",
    "L" : ".-..", "Y" : "-.--", "?" : "..--..",
    "M" : "--", "Z" : "--..", "\'" : ".-..-.", "/" : "-..-."
    }

# # #
# input should be word or morse - otherwise quit
# given a word(string)
# iterate through the word
# each iteration should show the value of the coinciding key in morse dict
# print the final list with the tranlated version of the string.
# -
# if input is morse:
# iterate through input
# find coincidence with key in morse dict
# store values of key
# show storage as string
# # #

def translating_to_morse ():
    text = input("\nIntroduce text to translate: ").upper()
    translation = []
    for i in text:
        if i == " " or i == string.punctuation:
            continue
        elif i in morse_dict.keys():
            translation.append(morse_dict.get(i))
        else:
            print ("Unable to translate: '",i,"' Please try again. Use only letters and/or numbers!")
            break
    translation = "    ".join(translation)
    return translation


def translating_to_natural():
    text = input("\nIntroduce MORSE to translate: ").strip().split()
    print (text)
    translation = []
    for i in text:
        for k,v in morse_dict.items():
            if i == v:
                translation.append(k)
    translation = "".join(translation)    
    return translation



def evaluate (text):
    if text == 1:
        print(translating_to_morse())
    elif text == 2:
        print(translating_to_natural())
    else:
        return print("\nChoose a valid option!")


def run ():
    print ("""
Welcome to TransMorse!
Are you ready to begin?
    """)
    while True:
        dec = input ("Yes/No\n").lower()
        if dec == "y" or dec == "yes":
            type_of_text = input("""
    Choose your option:
        1- Translating to morse
        2- Translating to natural language
        (1/2):
        """)
            try:   
                evaluate (int(type_of_text))
            except ValueError:
                print("\nChoose a valid option(number)")
            print("\nRestart?")
        else:
            break

    print ("\nThanks for using our services!\n")

if __name__ == '__main__':
    run()