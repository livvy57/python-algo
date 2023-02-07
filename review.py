tn = int(input())
cnt = tn

for _ in range(tn):
    txt = list(input())
    dict = list(set(txt))
    dict2 = ''.join(dict)
    for w in dict:
        if txt.count(w) >= 2:
            dup = list(dict2.index(w))

            if dup[-1] - dup[0] >= 2:
                cnt -= 1
print(cnt)