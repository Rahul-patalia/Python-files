# def insert_into_array(size):
#     a = []
#     for x in range(size):
#         a.append(int(input("Enter Number :")))

#     print(a)

# insert_into_array(int(input("Enter Size of array :")))

def less_than_ten(size):
    lis = []
    for check in range(0,size):
        lis.append(int(input("Enter number :")))
    
    newlis = []
    for number in lis:
            if number >= 10:
                newlis.append(number)
            
    print(newlis)
# a = [10, 11, 12, 15, 5, 3, 8]
less_than_ten(int(input("Enter size of the list :")))
