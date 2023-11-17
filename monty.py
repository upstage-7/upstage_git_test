import random

num_simulation = int(input("몇회 실행하실건가요?"))
solutions = [0,0,1]
wins_in_change = 0
wins_in_stay = 0

for i in range(num_simulation):
    random.shuffle(solutions)
    
    choice = random.choice([0,1,2])
    
    for i in range(3):
        if choice != i and solutions[i] == 0:
            monty_choice = i
            break
    
    
    if solutions[choice] == 1:
        wins_in_stay +=1
    
    if solutions[choice] == 0:
        wins_in_change +=1
    
    
print(f"문을 바꿨을 때 맞출 확률 : {wins_in_change/num_simulation}")
print(f"문을 안바꿨을 때 맞출 확률 : {wins_in_stay/num_simulation}")