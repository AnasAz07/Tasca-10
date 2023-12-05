def bin_to_dec(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num

a =  input("Introdueix el número binari: ")
dec = bin_to_dec(a)
print("El numero binari passat a decimal dona {}".format(dec))
