def pattern_A(n):
    for i in range(1, n+1):
        pattern = ""
        for j in range(65, 65+i):
            pattern += chr(j)
        print(pattern)

    for i in range(n-1, 0, -1):
        pattern = ""
        for j in range(65, 65+i):
            pattern += chr(j)
        print(pattern)

pattern_A(3)
