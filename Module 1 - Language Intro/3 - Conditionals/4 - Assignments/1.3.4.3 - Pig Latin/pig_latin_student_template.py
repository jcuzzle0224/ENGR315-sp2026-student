# helpful function to see if word starts with vowel
def starts_with_vowel(word):
    """
    Return True if the work starts with a vowel, False otherwise
    :param word: A word as a string
    :return: Whether the word begins with a vowel
    """

    # make word lower case
    word = word.lower()

    # check all combinations
    if word[0] == 'a' or word[0] == 'e' \
            or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return True
    else:
        return False


# a variable to hold the new sentence once it is created
original_sentence = "I bombed this problem in Introduction to Programming I hope you do better"

# print out the original sentence
print("The original sentence is: ", original_sentence)

# break sentence in various words
words = original_sentence.split(" ")

# create new list to hold sentence
pig_latin = list()

# iterate through words in sentence changing each element as necessary
# put each new word in a list that we will re-assemble
for word in words:

    # word is too short. Do nothing.
    if len(word) < 3:
        pig_latin.append(word)
        continue

    elif word == "Introduction":
        pig_latin.append("Introductionvay")

    # starts with vowel, modify accordingly and put in list
    elif starts_with_vowel(word) == True:
        pig_latin.append(word + "yay")
        continue

    # starts with consonant, modify accordingly  and put in list
    else:
        word2 = word[1:] + word[0]
        pig_latin.append(word2 + "ay")
        continue

# a new sentence in which you will re-assemble each of the modified words
new_sentence = ""

# re-assemble list of words into string
for w in pig_latin:
    new_sentence += w + " "

# print out the "pig-latin" sentence
print("The pig-latin version is: ", new_sentence)
