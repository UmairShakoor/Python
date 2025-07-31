def main():
    try:
        a = int(input('Enter a number: '))
        return

    except Exception as e:
        print(e)
        return

    finally: # This will also runs even function has returned before this but if we not write finally: and only try to run print().. then it will not run bcz function is returned before it
        print('I am inside finally')

main()
