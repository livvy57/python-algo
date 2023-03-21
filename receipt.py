payment_r = int(input())
item_num = int(input())
items = []
for _ in range(item_num):
    x, y = map(int, input().split())
    items.append(x*y)
[print("Yes") if payment_r == sum(items) else print("No")]