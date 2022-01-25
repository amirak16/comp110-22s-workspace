"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730485037"

meaningful_word: str = input("Enter a 5-character word.")
if len(meaningful_word) != 5:
    print("Error: word must contain 5 characters") 
    exit()

meaningful_letter: str = input("Enter a single character.")


print("Searching for " + meaningful_letter + " in " + meaningful_word)

goodnumber: int = 0



if meaningful_word[0] == meaningful_letter:
    print(meaningful_letter + " found at index 0")
    goodnumber = goodnumber + 1

if meaningful_word[1] == meaningful_letter:
    print(meaningful_letter + " found at index 1")
    goodnumber = goodnumber + 1

if meaningful_word[2] == meaningful_letter:
    print(meaningful_letter + " found at index 2")
    goodnumber = goodnumber + 1

if meaningful_word[3] == meaningful_letter:
    print(meaningful_letter + " found at index 3")
    goodnumber = goodnumber + 1

if meaningful_word[4] == meaningful_letter:
    print(meaningful_letter + "  found at index 4")
    goodnumber = goodnumber + 1


print(goodnumber , " instances of", meaningful_letter , "found in" , meaningful_word)
