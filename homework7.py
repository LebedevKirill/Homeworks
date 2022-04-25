numbers = [1, 2, 3, 4, 2, 3, 1, 1, 1, 1, 3, 3, 4]
dict1 = {}
def func():
    counter = 0
    for i in range (1, 5):
        for t in range(0,13):
            if i == numbers[t]:
                counter +=1
            if t == 12:
                dict1[i] = counter
                print(f'Число:{i} встречается {dict1.get(i)} раз')
                counter = 0
                
func()


