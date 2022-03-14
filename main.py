print("----------------- Program Kasir Cafe Galaxy -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Roti Bakar - Rp. 10,000")
   print("2. Pisang Goreng - Rp. 10,000")
   print("3. Onion Ring - Rp. 8,000")
   print("4. Chicken Fingers -  Rp. 12,000")
   print("5. French Fries - Rp. 12,000")
   print("6. Sandwich - Rp. 12,000")
   print("7. Spaghetti Bolognese - Rp. 20,000")
  
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*10000
       print (porsi," porsi Roti Bakar = Rp", totalmkn)
       mkn=("Roti Bakar")
   elif nomor==2:
       totalmkn=porsi*10000
       print (porsi," porsi Pisang Goreng = Rp", totalmkn)
       mkn=("Pisang Goreng")
   elif nomor==3:
       totalmkn=porsi*8000
       print (porsi, " porsi Onion Ring = Rp", totalmkn)
       mkn=("Onion Ring")
   elif nomor==4:
       totalmkn=porsi*12000
       print (porsi, " porsi Chicken Fingers = Rp", totalmkn)
       mkn=("Chicken Fingers")
   elif nomor==5:
       totalmkn=porsi*12000
       print (porsi, " porsi French Fries = Rp", totalmkn)
       mkn=("French Fries")
   elif nomor==6:
       totalmkn=porsi*12000
       print (porsi, " porsi Sandwich = Rp", totalmkn)
       mkn=("Sandwich")
   elif nomor==7:
       totalmkn=porsi*20000
       print (porsi, " porsi Spaghetti Bolognese = Rp", totalmkn)
       mkn=("Spaghetti Bolognese")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Ice Tea - Rp. 10,000")
   print("2. Orange Juice - Rp. 10,000")
   print("3. Thai Tea - Rp. 10,000")
   print("4. Dalgona Coffee - Rp. 10,000")
   print("5. Cappucino -  Rp. 10,000")
   print("6. Americano - Rp. 7,000")
  
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*10000
       print (gelas," Ice Tea = Rp", totalmnm)
       mnm=(" Gelas Ice Tea")
   elif nomor==2:
       totalmnm=gelas*10000
       print (gelas, " Gelas Orange Juice = Rp", totalmnm)
       mnm=("Orange Juice")
   elif nomor==3:
       totalmnm=gelas*10000
       print (gelas, " Thai Tea = Rp", totalmnm)
       mnm=("Thai Tea")
   elif nomor==4:
       totalmnm=gelas*10000
       print (gelas, " Dalgona Coffee = Rp", totalmnm)
       mnm=("Dalgona Coffee")
   elif nomor==5:
       totalmnm=gelas*10000
       print (gelas, " Cappucino = Rp", totalmnm)
       mnm=("Cappucino")
   elif nomor==6:
       totalmnm=gelas*7000
       print (gelas, " Americano = Rp", totalmnm)
       mnm=("Americano")
 
   else:
      print("Pilihan tidak ada, silahkan masukan data lagi")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")