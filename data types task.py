word_one = input()
word_two = input()

def get_frequecies(word):
    freq = []
    for i in range(len(word)):
        count = 0; letter = ''
        for f in range(len(freq)):
            if word[i] == freq[f][0]:
                count += 1; letter = f
        if count == 0:
            freq.append([word[i], 1])
        else:
            freq[letter][1] += 1
    return(freq)

freq_one = get_frequecies(word_one)
freq_two = get_frequecies(word_two)
count = 0

for k in range(len(freq_one)):
    for l in range(len(freq_two)):
        if (freq_one[k][0] == freq_two[l][0]) and (freq_one[k][1] <= freq_two[l][1]):
            count += 1

if count == len(freq_one):
    print('yes')
else:
    print('no')