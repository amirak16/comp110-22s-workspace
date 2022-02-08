"""EX02 - Wordle - One shot step towards wordel."""

__author__ = "730485037"

secretword: str = "python"

guess: str = input(f"What is your {len(secretword)}-letter guess? ")

while len(guess) != len(secretword):
    guess = input(f"That was not {len(secretword)} letters! Try again:")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
    
currentLetterIndex: int = 0
chainOfBoxes: str = ""

while (currentLetterIndex < len(secretword)):
    if (guess[currentLetterIndex] == secretword[currentLetterIndex]):
        chainOfBoxes += GREEN_BOX
    else:
        foundletter: bool = False 
        boxes: int = 0 
        while boxes < len(secretword):
            if guess[currentLetterIndex] == secretword[boxes]:
                foundletter = True
            boxes += 1
        if foundletter is False:
            chainOfBoxes += WHITE_BOX
        else:
            chainOfBoxes += YELLOW_BOX
    currentLetterIndex += 1
            
print(chainOfBoxes)

if guess == secretword:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")