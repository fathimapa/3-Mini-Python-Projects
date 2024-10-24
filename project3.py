import random 
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPEREND = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERAND,MAX_OPEREND)
    rigth = random.randint(MIN_OPERAND,MAX_OPEREND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(rigth)
    answer = eval(expr)
    return expr , answer

wrong = 0
input("Press enter to start")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problems()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break

        wrong += 1
    
end_time = time.time()
total_time = round(end_time - start_time,2)

print("--------------------")
print(f"Nice Work! You finished in {total_time} seconds!")