for i in range(8):
    for j in range(8):
            print(" "if i+j & 1 else "█", end=" ")
    print("", end="\n")