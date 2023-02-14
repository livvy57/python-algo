num = int(input())
cnt = num
for i in range(num):
    word = input()

    dict = list(word)
    for j in range(len(dict)-1):
        if dict[j] == dict[j+1]:
            pass
        else:
            if dict[j] in dict[j+1:]:
                cnt -= 1
                break
print(cnt)