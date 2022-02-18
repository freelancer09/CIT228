print("Lets do addition!")
i = "y"
while i != "q":
    try:
        n1 = int(input("Please enter the first number: "))
        n2 = int(input("Please enter the second number: "))
        n3 = n1 + n2
        print(n1, "+", n2, "=", n3)
    except ValueError:
        print("Error: You can only add numbers!")
    except:
        print("Error: Unknown")
    else:
        i = input("Would you like to play again? (q to quit): ")