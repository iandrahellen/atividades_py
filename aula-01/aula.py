n1 = 5
n2 = 6
n3 = 6

if n1 > n2 and n1 > n3:
    print("n1 é maior que todos!")
elif n2 > n1 and n2 > n3:
    print("n2 é maior que todos!")
elif n1 >= n2:
    print("n1 e n2 são iguais e maiores")
elif n1 >= n3:
    print("n1 e n3 são iguais e maiores")
elif n2 >= n1:
    print("n2 e n1 são iguais maiores")
elif n2 >= n3:
    print("n2 e n3 são iguais e maiores")
else: 
    print("n3 é maior que todos!")
