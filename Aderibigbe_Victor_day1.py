def number_guess(maximumguesses, targetnumber):
    """this is a function that takes in two parameters for maximum number of guesses and target number and tells the
    user if the gus is too low or too high """
    for i in range(maximumguesses):
        print("please enter your guess. You have " + str((maximumguesses - i)) + " guesses left")
        guess = int(input())
        if guess == targetnumber:
            print("your guess is correct")
            break
        elif guess < targetnumber:
            print("your guess is too low")
        elif guess > targetnumber:
            print("your guess is too high")
    return abs(guess - targetnumber)


print("The difference between your guess and the real guess is")
print(number_guess(5, 20))

