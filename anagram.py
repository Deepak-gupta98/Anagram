str = ["eat","tea","tan","ate","nat","bat"]

list_str = []
n = len(str)
i = 0
while(i<len(str)):
    list_one = []
    list_one.append(str[i])
    j=i+1
    while(j<len(str)):
        if sorted(str[i]) == sorted(str[j]):
            list_one.append(str[j])
            str.remove(str[j])
        else:   j+=1
    list_str.append(list_one)
    i+=1
print(list_str)
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
