# Reto * CONTANDO PALABRAS
# ENUNCIADO:
# Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

# SOLUCION:
# crear un diccionario para almacenar palabras:cantidad
# separar el texto en palabras 
# iterar el diccionario:
    # si ya hay key con esa palabra:
        # value + 1
    # sino crear key:1
# mostrar dict
# mostrar cantidad total de palabras

# EJEMPLO:
#  "Hola, mi nombre es Leandro. Mi nombre completo es Leandro Luna. En lugar de Leandro, mis amigos me dicen Lean. Mis amigos son lo mas grande del mundo. Cuando yo sea grande seguro cambie mi nombre por uno mas especial para mí. Mi nombre actual me gusta pero creo que no me representa. No entiendo muy bien por que.-"
# "HOLA" = 1
# "MI" = x
# total = y

# imports para modificar el texto recibido
import re
from unicodedata import normalize   ## see example below

#### 1ro -  quitamos todos los caracteres especiales
# word = "apañárselas??# 6545 }{!}"
# mod1 = re.sub(r'[^\w\s]',"", word.strip().lower())
# print(mod1)
#### 2do -  quitamos tildes y normalizamos el texto
# mod2 = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", mod1), 0, re.I)
# print(mod2)

sample = "Hola, mi nombre es Leandro. Mi nombre completo es Leandro Luna. En lugar de Leandro, mis amigos me dicen Lean. Mis amigos son lo mas grande del mundo. Cuando yo sea grande seguro cambie mi nombre por uno mas especial para mí. Mi nombre actual me gusta pero creo que no me representa. No entiendo muy bien por que.-"

def modify_text(txt):
    mod1 = re.sub(r'[^\w\s]',"", txt.strip().lower()) 
    mod2 = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", mod1), 0, re.I) 
    final_text = mod2.split()
    return final_text

# print ("This is your text: \n",sample)
# print ("These are the words of your text separately: \n",modify_text(sample))
def counting_words(txt):
    words = {}
    for i in txt:               # iterating through the list
        if i not in words:      # if i of list not in dic:
            words[i] = 1        # we assign i to words[key] and 1 to words[value]
        else:                   # if i is in dic:
            words[i] += 1       # we add 1 to words[i] key
    for k,v in words.items():                                           # iterating through dic
        print ("The word '"+ str(k) +"' appears "+ str(v) +" times!")   # show each key and its value, in string format 
    return words

def run ():
    print ("\nWelcome to TEXT ANALYSER! Are you ready to start?")
    while True:
        decision = input("Yes/No\n").upper()
        if decision in ["Y","YES"]:
            text = input("\nIntroduce text here: \n")
            print ("\nThis is your text: \n",text)
            text_words = modify_text(text)
            print ("\nThese are the words of your text separately: \n",text_words,"\n")
            counting_words(text_words)
            print ("\nStart again?")
        else: 
            break
    
    print ("\nThanks for using TEXT ANALYZER!!!\n")


if __name__ == "__main__" :
    run()