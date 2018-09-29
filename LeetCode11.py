while True:
    try:
        a, b = map(int, input("please input 2 int type: ").split())
        print(a+b)
    except ValueError:
        print("Please input invalid type(int)")
