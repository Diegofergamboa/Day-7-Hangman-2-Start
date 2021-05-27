#Libreria random
import random
#Lista con palabras random
word_list = ["aardvark", "baboon", "camel"]
#Seleccion aleatoria de la palabra 
chosen_word = random.choice(word_list)
#Conversion de la palabra aleatoria escogida a lista
display = list(chosen_word)
print(display)

word_lenght = len(display)    
user_choice = input('Choose a letter: ') 

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
    
    
for position in range(word_lenght):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == user_choice:
        display[position] = letter




for position in range(word_lenght) :
    letter = display[position]
    
print(display)