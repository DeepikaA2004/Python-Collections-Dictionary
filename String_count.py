def count_letters(S):
    letter_count = {}
    
    for char in S:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    return letter_count

S = input()
d = count_letters(S)
d1 = {}
for i in S:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
if d1 == d:
    print('yes')
else:
    print('no')