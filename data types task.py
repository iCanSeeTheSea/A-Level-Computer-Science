word_one = list(input())
word_two = list(input())
check_list = [['', 0]]
count = 0
count_one = [['', 0]]

for k in range(len(word_one)):
    for h in range(len(count_one)):
        if count_one[h] == word_one[k]:
            

for i in range(len(word_two)):
    for k in range(len(word_one)):
        if word_two[i] == word_one[k]:
            count = 0
            for l in range(check_list):
                if check_list[l][0] == word_one[k]:
                    count += 1
            check_list.append([word_two[i], count])
        else:
            pass
    

if len(check_list)-1 == len(word_one):
    print('yes', check_list, word_one)        
else:
    print('no', check_list, word_one)