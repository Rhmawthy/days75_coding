a = int(input("masukkan angka :"))

b =[i for i in range(1,a+1)]

print (b)

if a <= 8:
    print("angka yang anda masukkan masih terlalu kecil")
elif a <= 8 and a >= 28:
    print("good")
else:
    print("out of range")




