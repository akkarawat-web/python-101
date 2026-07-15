
test1 = float(input("Enter the score for test 1: "))
test2 = float(input("Enter the score for test 2: "))
test3 = float(input("Enter the score for test 3: "))


average = (test1 + test2 + test3) / 3


print(f"The average score is {average:.1f}")


if average >= 90:
    print("Congratulations!")
    print("That is a great average!")