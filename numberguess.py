import random
 
 
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"
 
 
def banner():
    print(C.CYAN + C.BOLD + "=" * 40 + C.RESET)
    print(C.CYAN + C.BOLD + "       NUMBER GUESSING GAME" + C.RESET)
    print(C.CYAN + C.BOLD + "=" * 40 + C.RESET)
    print(C.GRAY + "I'm thinking of a number between 1 and 100." + C.RESET)
    print()
 
 
def main():
    target = random.randint(1, 100)
    attempts = 0
    low, high = 1, 100
 
    banner()
 
    while True:
        print(C.GRAY + f"Range: {low}-{high}  |  Attempts: {attempts}" + C.RESET)
        guess_input = input(C.BOLD + "> Your guess: " + C.RESET).strip()
 
        if not guess_input.isdigit():
            print(C.YELLOW + "Please enter a valid number." + C.RESET)
            print()
            continue
 
        guess = int(guess_input)
        attempts += 1
 
        if guess < target:
            print(C.RED + "Too low!" + C.RESET)
            if guess > low:
                low = guess
        elif guess > target:
            print(C.RED + "Too high!" + C.RESET)
            if guess < high:
                high = guess
        else:
            print()
            print(C.GREEN + C.BOLD + "=" * 40 + C.RESET)
            print(C.GREEN + C.BOLD + f"  Correct! The number was {target}." + C.RESET)
            print(C.GREEN + C.BOLD + f"  Solved in {attempts} attempt{'s' if attempts != 1 else ''}." + C.RESET)
            print(C.GREEN + C.BOLD + "=" * 40 + C.RESET)
            break
 
        print()
 
 
if __name__ == "__main__":
    main()
 