name = input("Hi! What's your name? ")

print()

print("Nice to meet you " + name + ", lets play a game!")

print()

print("This game is almost (exactly) like Madlibs.")
play = input("Do you know how to play? Type 'y' for yes or 'n' for no ")

if play == "y":
  print("Great! Let's get started.")
elif play == "n":
  print()
  print("You will input the asked items (it may be a number, color, verb, adjective, or something else). \
            You will then recieve a Madlib, a random story based on your input items")
else:
    ifnotyorn = input("Please type in 'y' for yes or 'n' for no ")

print("Please input:")

print()

person = input("A person ")
place = input("A place ")
adjectivea = input("An adjective ")

print()

place = input ("Same place as the first ")
pluralnouna = input("A plural noun ")
adjectiveb = input("An adjective ")
pluralnounb = input("A plural noun ")

print()

place = input("Same place as the first ")
actionverb = input("An action verb ")
pluralnounc = input("A plural noun ")
pluralnound = input("A plural noun ")
noun = input("A noun ")

madlib33 = ("Last summer, my mom and dad took me and " + person + " on a trip to " + place +\
                "." " The weather there is very " + adjectivea + ".")

madlib66 = (" Northern " + place + " has many " + pluralnouna + " and they make " + adjectiveb +\
                " " + pluralnounb + " there.")

madlib99 = (" Many people also go to " + place + " to " + actionverb + " or see the " + \
                pluralnounc + "." + " The people who live there love to eat " + pluralnound +\
                 " and are very proud of their big " + noun)

print("I know that was long, but we're done! Lets get your Madlib...")
print(madlib33 + madlib66 + madlib99)

print()

print("Did you like the game? :^) ")
