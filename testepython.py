# Declarando variáveis

export = open("export.json","w") # Criando arquivo que receberá os valores

hour_initial = str(input("Hour Initial: ex: '00:00' "))
print (hour_initial)
hour_end = str(input("Hour End: ex: '23:59' "))
print (hour_end)
minimum_fare_equation = float(input("Minimum Fare Equation: ex: '2.30' "))
print (minimum_fare_equation)
boarding_fee_equation = float(input("Boarding Fee Equation: ex: '5.90' "))
print (boarding_fee_equation)
price_per_kilometer_equation = float(input("Price per Kilometer Equation: ex: '0.10' "))
print (price_per_kilometer_equation)
price_per_minute_equation = float(input("Price per Minute Equation: ex: '4.30' "))
print (price_per_minute_equation)
rounding_factor_equation = float(input("Rounding Factor Equation: ex: '2.45' "))
print (rounding_factor_equation)
waiting_time = bool(input("Waiting time: True or False "))
print (waiting_time)
is_active = bool(input("Is Active? "))
print (is_active)
typev = str(input("Type: ")) # Variável type precisei declarar como typev
print (typev)
minimum_speed = int(input("Minimum Speed: ex: '80' "))
print (minimum_speed)
minimum_bearing = int(input("Minimum Bearing: ex: '30' "))
print (minimum_bearing)
minimum_accuracy = int(input("Minimum Accuracy: ex: '10' "))#Recebo erro informando que precisa ser str e nao int para gravar no json :(
print (minimum_accuracy)
export.write("hour_initial: " + hour_initial +"\n" +  
             "hour_end: " + hour_end + "\n" +
             "minimum_fare_equation: " + str(minimum_fare_equation) + "\n" +
             "boarding_fee_equation: " + str(boarding_fee_equation) + "\n" +
             "price_per_kilometer_equation: " + str(price_per_kilometer_equation) + "\n" +
             "price_per_minute_equation: " + str(price_per_minute_equation) + "\n" +
             "rounding_factor_equation: " + str(rounding_factor_equation) + "\n" +
             "waiting_time: " + str(waiting_time) + "\n" +
             "is_active: " + str(is_active) + "\n" +
             "type: " + typev + "\n" +
             "minimum_speed: " + str(minimum_speed) + "\n" +
             "minimum_bearing: " + str(minimum_bearing) + "\n" +
             "minimum_accuracy: " + str(minimum_accuracy)
             )

export.close()
print ("dados exportados com sucesso")




