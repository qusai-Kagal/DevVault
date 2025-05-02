import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERANDS = 3
MAX_OPERANDS = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter to start the quiz...")
print("-- Start of the quiz --")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        try:
            if int(guess) == answer:
                break
            else:
                print("Incorrect. Try again.")
                wrong += 1
        except ValueError:
            print("Please enter a valid number.")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("\n-- End of the quiz --")
print("Nice work! You finished the quiz in", total_time, "seconds!")
print("Wrong attempts:", wrong)
print("Your score is", (TOTAL_PROBLEMS - wrong) * 10, "%")