with (
    open('f1.txt', 'w') as f1,
    open('f2.txt', 'w') as f2
):
    msg = 'I am a Hacker'
    f1.write(msg)
    f2.write(msg)
