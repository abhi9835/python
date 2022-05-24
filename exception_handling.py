while True:
    print("press q to quit")
    a = int(input())

    try:
        print('Trying...')
        a = int(a)
        if a > 6:
            print('the number is greater than 6')
    except Exception as e:
        print(f"your input resulrted in an error: {e}")

print("Thanks for playing this game")