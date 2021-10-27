#looplardan foydalangan holda kopaytiruv amalini bajarish
a = int(input("1 - sonni kiriting: "))
b = int(input("2 - sonni kiriting: "))
jami = 0
c = 0
while(a >= b):
    if(c < b):
        jami += a
        c += 1
    else:
        break
print(jami)