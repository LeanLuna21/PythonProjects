# Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#  *        variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "?".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "x".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.

# Planeacion:
#  ___|___|___|___|___
#  3 run 1 jump
#  run in | = x
#  jump in _ = ?

# given a track:
# input steps (run or jump(r o j))
# compare steps with track:
    # if match -> move forward - print track
    # if !=:
        # evaluate 
            # if run in | -> x
            # if jump in _ -> ?
# if all steps match track:
    # won
# else keep repeating until done

given_track = "___|___|___"

def user_options():
    step = 0
    user_track = []
    while step < len(given_track):
        user_step = input("Would you like to run or jump? (Insert r or j): ").lower()
        if user_step == "r" or user_step == "j":
            print(f"Current step: {step} // Your step: {user_step}")
            user_track.append(user_step)
            step += 1
        else: 
            print("Choose a valid character (r or j)")
    return "".join(user_track)

def creating_track(options):
    user_track = ""
    for i in options:
        if i == "r":
            user_track += "_"
        else:
            user_track += "|"
    return user_track

def comparing_tracks(given_track,user_track):
    solution = ""
    for i,step in zip(user_track,given_track):
        if i == step:
            solution += i
        else:
            if i == "_" and step == "|":
                solution += "x"
            if i == "|" and step == "_":
                solution += "?"
    return solution


def run():
    choice = (input("""
Welcome to racing guessing!
\nIn this game you will be running through a track with stocks while blindfolded.
\nIn the end, you'll see if you have made the right move, or if you crashed a stock ("x") or jumped when it wasn't necessary ("?").
Do you think you can beat the track in the dark?
Let us see...
\nAre you ready to start?: (y/n) """).lower())
    if choice == "y":
        print("Let's begin!")
        user_track = creating_track(user_options())
        solution = comparing_tracks(given_track,user_track)
        print (solution)
        if solution == given_track:
            print("\nPERFECT! You have reached the end of the line unharmed! CONGRATS!")
            if input("Play again? (y/n): ").lower() == "y":
                run()
            else:
                print("Ok, champ! Later!")
                quit()
        else:
            choice2 = input("\nOh it seems you got some steps wrong! Are you hurt? No? GREAT. Give it another try? (y/n): ")
            if choice2  == "y":
                run()
            else:
                print("Ok! COWARD...")
                quit()
    else:
        print("OK next time it'll be then... COWARD!")


if __name__ == "__main__":
    run()





