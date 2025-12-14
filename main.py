import random
Lletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

UL = int(input("How many upper case letters do you want in your password? : \n"))
LL = int(input("How many lower case letters do you want in your password? : \n"))
N = int(input("How many numbers do you want in your password? : \n"))
S = int(input("How many symbols do you want in your password? : \n"))

PL = []
password = ""

for i in range(0,LL):
    PL.append(random.choice(Lletters))
for i in range(0,UL):
    PL.append(random.choice(Uletters))
for i in range(0,N):
    PL.append(random.choice(numbers))
for i in range(0,S):
    PL.append(random.choice(symbols))

TL = LL + UL + N + S
random.shuffle(PL)

for i in PL:
    password += i

print("Your password is : ",password)
