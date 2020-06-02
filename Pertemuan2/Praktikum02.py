pins = {"Reza":1234, "Mamat":1111,"Riski":2222}
pins["Reza"]
pins.keys()


masukan = input("Masukan nama anda : ")
print('Nama anda adalah : ',masukan)

bilangan = int(input("Masukan Bilangan : "))
print('Jika bilangan ',bilangan,'dikuadratkan adalah : ',bilangan**2)

bil = float(input("Masukan bilangan pecahan : "))
print('Jika bilangan ',bil,'dibagi 2 adalah : ',bil/2)


x = input("Masukan nilai pertama : ")
y = input("Masukan nilai kedua : ")

print("\nNilai pertama : ",x)
print("Nilai kedua   : ",y)

if(x>y):
	print("\nNilai pertama lebih besar daripada nilai kedua",x,">",y)
else:
	print("\nNilai pertama lebih kecil daripada nilai kedua",x,"<",y)


print("======= Menentukan keadaan air =======\n")
suhu = int(input("Masukan suhu air : "))
if(suhu>100):
	print("Dalam suhu ini air berwujud gas ")
elif(suhu > 0 and suhu <100):
	print("Dalam suhu ini air berwujud zat cair")
else:
	print("Dalam suhu ini air akan berwujud es")


def keliling(s):
	return 4*s

def luas(s):
	print("Luasnya adalah : ",s*s)

print("======== Menghitung Luas & Keliling Persegi ========\n")
x = int(input("Masukan panjang sisi persegi :"))
print("Kelilingnya adalah : ",keliling(x))
luas(x)

def PenentuNilai(nilai):
	if(nilai<= 100 and nilai >= 80):
		print("Maka anda mendapat A ")
	elif (nilai <80 and nilai >=70):
		print("Maka anda mendapat B")
	elif(nilai <70 and nilai >=60):
		print("Maka anda mendapat C")
	elif(nilai < 60 and nilai >=40):
		print("Maka anda mendapat D")
	elif(nilai <40 and nilai >=0):
		print("Maka anda mendapat E")
	else:
		print("Format yang anda masukan salah")

bilangan = int(input("Masukan Nilai : "))
print ("Jika nilai anda ",bilangan)
PenentuNilai(bilangan)
