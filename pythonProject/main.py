import random
import time

random.seed(time.time())

name = input("Write your name (for the score): ")
category = input("Choose a category from colors/food/names/sport: ")
# print(category)
word = ""
list = []
try:
    category_lists = "categories/" + category + ".txt"
    f = open(category_lists)
    for line in f:
        list.append(line.strip())
    # print(sport)
    word = random.choice(list)
    # print(word)
    f.close()
except:
    print("Unable to open file")

mistakes = 0
max_tries = len(word)
# print(max_tries)
word_to_print = ""
for l in word:
    word_to_print = word_to_print + "_"
print(word_to_print)

while mistakes < max_tries:
    print("Enter your letter")
    print("You have " + str(max_tries - mistakes) + " chances left")
    letter = input("Your letter is: ")
    for l in range(len(word)):
        if word[l] == letter:
            new_word = word_to_print[:l] + letter + word_to_print[l + 1:]
            word_to_print = new_word
    if letter not in word:
        mistakes = mistakes + 1
    if word_to_print == word:
        print("You won! The word was " + word + ". You made " + str(mistakes) + " mistakes")
        break
    print(word_to_print)
    print("______________________________________________________________")

if mistakes >= max_tries:
    print("You lost! The word was " + word + ". You made " + str(mistakes) + " mistakes")

try:
    f = open("score.txt", mode="a")
    f.write("The player " + name + " had the score: " + str(len(word) - mistakes) + "\n")
    f.close()
except:
    print("Unable to open file score.txt")
