import random
random_number = random.randint(3, 20)
print('ЧИСЛО ИЗ ПЕРВОЙ ВСТАВКИ:',random_number)
result_=[]
i=1
while i<20:
#for i in range(1,20):
    for k in range(1,20):
        if k == 1:
            k+=1
            continue
        if i == k:
            continue
        if k<i:
            continue
        if random_number == i+k or random_number%(i+k) == 0:
            result_.append(i)
            result_.append(k)
    i+=1

print('Нужный пароль----',*result_)