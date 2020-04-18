def reverse(num):
    revd = 0
    while num > 0:
        digit = num % 10
        revd = (revd * 10) + digit
        num = num // 10

    return revd
    
while True:
    promt = "Enter any number to revser it:"
    num = int(input(promt))
    
    rev = reverse(num)

    print(rev)
    
    