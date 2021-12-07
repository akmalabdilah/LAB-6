import math
# perbedaan antara def() dengan lambda().
def a(x):
    return x**2
 
print("===========SELAMAT DATANG=============")

lambda_a = lambda x: x**2
 
# pemanggilan def() dan lambda()
# mencetak hasil pada def()
print(a(10))
 
# mencetak hasil pada lambda()
print(lambda_a(10))

print("=================LANJUT===============")

# perbedaan antara def() dengan lambda()
def b(x, y):
 return math.sqrt(x**2 + y**2)

lambda_b = lambda x, y: x**2 + y**2

# pemanggilan def() dan lambda()
# mencetak hasil pada def()
print(b(10,10))
 
# mencetak hasil pada lambda()
print(lambda_b(10,10))

print("=================LANJUT===============")

# perbedaan antara def() dengan lambda()
def c(funct,*args):
    funct(*args)
def pesan_awal(sum):
    return print (sum)
def pesan_akhir(len):
    return print(len)
c(pesan_awal, 'Selamat Belajar Kawan')
c(pesan_akhir, 'Lambda Python \n')
c(lambda: pesan_awal('Selamat Belajar Kawan'))
c(lambda: pesan_akhir('Lambda Python'))

print("=================LANJUT===============")
def d(set,*s):
    set(*s)
def pesan_awal(join):
    return print (join)
def pesan_akhir(b):
    print(b)
d(pesan_awal, 'Selamat Jalan Kenangan')
d(pesan_akhir, 'Kekurangan Dalam Program \n')
d(lambda: pesan_awal('Selamat Jalan Kenangan'))
d(lambda: pesan_akhir('Kekurangan Dalam Program'))
print("=======SELESAI SAMPAI JUMPA LAGI======")


