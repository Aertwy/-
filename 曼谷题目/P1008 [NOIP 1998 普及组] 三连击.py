for a in range(123, 334):
    b =a*2
    c =a*3
    ai=(str(a)+str(b)+str(c))

    if "0" not in ai and len(set(ai)) == 9:
        print(ai)

