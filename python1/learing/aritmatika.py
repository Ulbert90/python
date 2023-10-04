#oprasi artimatika

a = 10
b = 3

#oprasi pertambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

#oprasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

#oprasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#oprasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#oprasi eksponen(pangkat)**
hasil = a ** b
print(a,'**',b,'=',hasil)

#oprasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

#oprasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas oprasi, 
"""
    1. ()
    2. eksponen **
    3. perkalian dkk */ ** % //
    4. pertambahan dan pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x * y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//','=', hasil)

print("===CONTOH===")
hasil = x + x * y
print (x,'+',x,'*',y,'=',hasil)