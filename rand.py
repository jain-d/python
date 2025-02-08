import random, math, threading

red = "\033[31m"
green = "\033[32m"
yellow = "\033[38;5;11m"
blue = "\033[38;5;33m"
orange = "\033[38;5;208m"
reset = "\033[0m"

def code_generation():
    i = 0
    lastNumber = 0
    code = 0
    while i < 6:
        while True:
            randomNumber = math.floor(random.random() * 10)
            if randomNumber == lastNumber:
                continue
            break
        code = (code * 10) + randomNumber
        lastNumber = randomNumber
        i += 1
    return code

def main():
    code = code_generation()
    print(f"\n\t{orange}{code}{reset}")
    """
    userInput = input(f"\nplease enter the code => {yellow}")

    if (userInput == str(code)):
        print(f"\n{reset}Access {green}GRANTED{reset}\n")
    else:
        print(f"\n{reset}Access {red}DENIED{reset}\n")
    """  
    threading.Timer(12.0, main).start()

main()
