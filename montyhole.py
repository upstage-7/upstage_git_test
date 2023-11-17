import random

n=int(input("반복할 횟수를 입력하세요: "))

origin,change=0,0

for i in range(n):
    doors=[0,0,1]
    random.shuffle(doors)
    
    # 내가 선택
    choose=doors[0]
    # 내가 선택한거 우선 뺴고
    doors=doors[1:]
    # 염소하나 제거
    doors.remove(0)
    
    if choose==1:origin+=1
    else:change+=1
    
print("안바꿨을 때 뽑았을 확률:",origin/n)
    
    