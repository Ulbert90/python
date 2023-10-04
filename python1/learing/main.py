data_interger = 1
print("Data : ", data_interger)
print("- bertipe : ", type(data_interger))

data_string = ("welowelweo")
print("Data : ",data_string)
print("- bertipe : ", type(data_string))

data_float = 1.5
print("Data : ", data_float)
print("- bertipe : ", type(data_float))

data_bool = True
print("Data : ", data_bool)
print("- bertipe : ", type(data_bool))

#tipe data C
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print("- bertipe : ", type(data_c_double))