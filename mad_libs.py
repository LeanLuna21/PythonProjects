""" 
'Mad libs' es un juego en el que dado un parrafo con espacios en blanco, se completan los espacios en blanco con palabras que pueden ser adj, sust, vbs, etc. para crear una historia loca. Esas palabras se le piden al jugador, y luego se muestra la historia completa.

1. Create paragraph for story in a variable
2. think of the words needed
3. each replaced word will be assigned to a variable
4. each variable will depend on user's input
5. each variable should contain a prompt message for the user to know which type of word they need
6. replace words in paragraph by variables through concatenation (f "Text {variable} text..." )
7. show final result (print())
"""

def main():
    print("\nWelcome to Mad Libs!! \n First, you need to complete some information... and then you'll get your story. \n\n Choose the story you would like to complete: \n   [1] -> Pizza time \n   [2] -> Your future.")
    choice = int(input(":"))
    try:
        print ("\nYou have chosen: " + choosing_story(choice)+"!")
        if choosing_story(choice) == "Pizza Time":
            pizza_time()
        elif choosing_story(choice) == "Your Future":
            your_future()
        print ("\nHope you've had a good laugh!! Later!\n")
    except:
        print ("\nChoose a valid number!\n")

def choosing_story(n):
    if n == 1:
        return "Pizza Time"
    elif n == 2:
        return "Your Future"
    else:
        print ("The story you are choosing is not available at the moment.")

def pizza_time():
    start = True
    while start:
        adj1 = input("Give me an adjective: ")
        nationality = input("Nationality: ").capitalize()
        name = input("A name: ").capitalize()
        noun1 = input("A noun: ")
        adj2 = input("Give me an adjective: ")
        noun2 = input("A noun: ")
        adj3 = input("Give me an adjective: ")
        adj4 = input("Give me an adjective: ")
        noun_pl = input("Now a plural noun: ")
        noun3 = input("A noun: ")
        number1 = input("A number: ")
        shape_pl = input("A shape: ")
        shape_pl = shape_pl+"s"
        food1 = input("Some food: ")
        food2 = input("Some food: ")
        number2 = input("Another number: ")
        
        mad_lib1 = (f"\nPizza was invented by a {adj1} {nationality} chef named {name}. To make a pizza, you need to take a lump of {noun1}, and make a thin, round {adj2} {noun2}. Then you cover it with {adj3} sauce, {adj4} cheese, and fresh chopped {noun_pl}. Next you have to bake it in a very hot {noun3}. When it's done, cut it into {number1} {shape_pl}. Some kids like {food1} pizza the best, but my favorite is the {food2} pizza. If I could, I would eat pizza {number2} times a day.\n")
        
        print (mad_lib1)
        start = False

def your_future():
    start = True
    while start:
        job = input ("Tell me a job: ")
        adj1 = input ("An adjective: ")
        city = input ("A city and country: ").capitalize()
        adj2 = input ("Another adjective: ")
        verb = input ("An -ing verb: ")
        name = input ("Give me a name: ").capitalize()
        description = input ("A description: ")
        superlative = input ("A superlative adjective: ")

        mad_lib2 = (f"""\nA: I can tell the future!

B: What will my life be like in the year 2030? What job will I do?

A: You will be a {job}. You will think its {adj1}

B: Really? Where will I live?

A: You'll live in {city}, and you'll be very {adj2}

B: Will I be famous?

A: Yes. You will be famous for {verb}

B: Wow!! Who will I marry?

A: You will marry a boy / girl called {name}. - You will live in a {description} house and have the {superlative} children in theworld!""")

        print (mad_lib2)
        start = False

if __name__ == "__main__":
    main ()
