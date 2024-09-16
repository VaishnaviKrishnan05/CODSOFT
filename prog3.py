import random
let=['a','b','c','d','e','f','g','h','i','j','k','l',
     'm','n','o','p','q','r','s','t','u',
     'v','w','x','y','z','A','B','C','D','E','F','G',
     'H','I','J','K','L','M','N','P','Q','R','S','T',
     'U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','&','(',')','*','+']
print('*GENERATE YOUR PASSWORD USING PYTHON*')
let_1=int(input('Enter the number of letters you want in your password :'))
num_1=int(input('Enter the number of digits you want in your password :'))
sym_1=int(input('Enter the number of symbols you want in your password :'))
pas=[]
for i in range(1,let_1):
    char=random.choice(let)
    pas += char
print(pas)

for i in range(1,num_1):
    char=random.choice(num)
    pas += char
print(pas)

for i in range(1,sym_1):
    char=random.choice(sym)
    pas += char
print(pas)
random.shuffle(pas)
print(pas)

pas1 = "".join(pas)
print("Your generated password is:", pas1)
