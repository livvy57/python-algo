while True:
    print("------------------")
    print("1. 더하기")
    print("2. 빼기")
    ans = 0
    mode = int(input("입력 모드를 선택하세요: "))
    a, b = map(int, input("두 개의 숫자를 입력하세요: ").split())
    if mode == 1:
        ans = a+b
    if mode == 2:
        while True:
            if a >= b:
                ans = a-b
                break
            print("결과 값이 음수입니다. 다시 값을 입력하세요.")
            a, b = map(int, input("두개의 숫자를 입력하세요: ").split())
    print("Calculation Results: ", ans)

