"""EX03 - Wordle - Implemeting main function towards wordel's game loop."""
 
__author__ = "730485037"
 
 
def contains_char(ss: str, sc: str) -> bool:          # ss= single string and sc= single character
    """Generates a character that is being searched for in the string of the second parameter.""" 
    assert len(sc) == 1
 
    foundletter: bool = False
    boxes: int = 0
  
    while boxes < len(ss):
        if sc == ss[boxes]:
            foundletter is True
            return True
        else:
            boxes += 1
    return False
 
 
def emojified(gp: str, sp: str) -> str:         # gp= guess parameter and sp secret parameter
    """A string of emoji."""
    assert len(gp) == len(sp)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"  
    YELLOW_BOX: str = "\U0001F7E8"
  
    i: int = 0
    chainOfBoxes: str = ""
 
    while i < len(sp):
        if contains_char(sp, gp[i]) is True:
            if(gp[i] == sp[i]):
                chainOfBoxes += GREEN_BOX
            i += 1
        else:
            chainOfBoxes += YELLOW_BOX
            i += 1
    else:
        chainOfBoxes += WHITE_BOX
        i += 1
    return chainOfBoxes
  
 
def input_guess(gp: int) -> str:      
    """Provide a guess for expected length."""
    guess: str = input(f"Enter a {gp} character word: ")
 
    while gp != len(guess):
        guess = input(f"That wasn't {gp} chars! Try again: ")
    return guess
 
 
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    t = 1
    counter: bool = True
    while counter is True:                   # t = turn
        print(f"== Turn {t}/6 === ")
        guess_word: str = input_guess(len(secret_word))
        if guess_word == secret_word:
            print(f"You won in {t}/6 turns!")
            print(emojified(guess_word, secret_word))
            counter = False
        else:
            print(emojified(guess_word, secret_word))
            t += 1
        if t == 6:
            print(f"== Turn {t}/6 === ")
            guess_word: str = input_guess(len(secret_word))
            if guess_word == secret_word:
                print(f"You won in {t}/6 turns!")
                print(emojified(guess_word, secret_word))
                counter = False
            else:
                print(emojified(guess_word, secret_word))
                print("X/6 - Sorry, try again tomorrow!")
                counter = False
    
 
if __name__ == "__main__":
    main()