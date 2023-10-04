#input data user

#data yang di masukan pasti string
data = input("masukan data: ")

print("data =", data, "type =", type(data))

#jika ingin mengambil int/float 
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))

print("data =", angka, ",type =", type(angka))

#boolean/ true/false /0/1
biner = bool(int(input("masukan nilai boolean")))

print("data =", biner, "type =", type(biner))