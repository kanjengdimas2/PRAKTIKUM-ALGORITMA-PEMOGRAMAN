#Celcius to Fahrenheit, Reamur, Kelvin  
print("Celcius-fahrenheit, Reamur, Kelvin")
celcius = int(input("masukkan suhu celcius "))
fahrenheit = (celcius * 9/5) + 32
reamur = (4/5 * celcius)
kelvin = (celcius + 273,15)

print("rumus celcius-fahrenheit : 9/5 x celcius x 32")
print("rumus celcius-reamur : 4/5 * celicus")
print("rumus celcius-kelvin : celcius + 273,15")
print("fahrenheit adalah",fahrenheit)
print("reamur adalah", reamur)
print("kelvin adalah", kelvin)