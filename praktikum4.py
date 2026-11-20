hari1 = {"keju", "tepung", "garam", "gula", "coklat"}
hari2 = {"garam", "gula", "coklat", "kecap"}

hari2.add("keju")

print("3. Sama:", hari1.intersection(hari2))        

print("4. Hari1 saja:", hari1.difference(hari2))    

hari1.remove("garam")

print("6. Hari2 saja:", hari2.difference(hari1))    

print("7. Tidak sama:", hari1.symmetric_difference(hari2))   

print("8. Hari pertama:")
for barang in hari1:
    print("-", barang)

print("9. Hari kedua:")
for barang in hari2:
    print("-", barang)