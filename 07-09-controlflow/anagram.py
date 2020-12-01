import json
import random
 
def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word
 
def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled
        
if __name__ == "__main__":
    filename = '/home/oem/Documents/days/07-09-controlflow/file.json'
    # file = open(filename)
    # print(file)
    with open(filename) as f:
        data = json.load(f)
    # data = json.load(file)
    
    print("Welcome to the Anagram Game!")
    while(True):
        word = word_prompt(data, 5)
        question = shuffle_word(word)
        meaning = data[word]
        
        question = question.lower()
        word = word.lower()
        print("\nSolve:", question)
        print("Hint:", meaning)
 
        for i in range(5, 0, -1):
            print("Attempts Left:", i)
            guess = input('Make a guess: ').lower()
            if guess == word:
                print("Correct!")
                break
            if i == 1:
                print("Correct Answer:", word)
        
        choice = input("\nContinue? [y/n]: ")
        print('-'*50)
        if choice == 'n':
            print("\nThank you for playing!")
            break