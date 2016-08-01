#-*- coding: utf-8 -*-

#export = open("export.json","w") # Criando arquivo que receberá os valores

hour_initial = float("%.2f"%input("Hour Initial: ex: '00.00' "))
print (hour_initial)
hour_end = float("%.2f"%input("Hour End: ex: '23.59' "))
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
typev = str(raw_input("Type: ")) # Variável type precisei declarar como typev
print (typev)
minimum_speed = int(input("Minimum Speed: ex: '80' "))
print (minimum_speed)
minimum_bearing = int(input("Minimum Bearing: ex: '30' "))
print (minimum_bearing)
minimum_accuracy = int(input("Minimum Accuracy: ex: '10' "))#Recebo erro informando que precisa ser str e nao int para gravar no json :(
print (minimum_accuracy)

#Iniciando processo de exportacao JSON

import json
modelo = {
             "taximeters" : [
           {
             "formulas" : [
                  {
                  "fare" : "day_fare",
                  "hour_initial" : hour_initial,
                  "hour_end" : hour_end,
                  "equation" : "round(max(12,(boardingFee+(0.3*durationInMinute)+(0.95*distanceInKm))),1)",
                  "identifier" : "taximeter_day_fare_v1",
                  "boarding_fee" : boarding_fee_equation
                  }
            ],
            "service" : "regular",
            "type" : typev,
            "waiting_time" : waiting_time,
            "is_active" : is_active,
            "minimum_speed" : minimum_speed,
            "minimum_bearing" : minimum_bearing,
            "minimum_accuracy" : minimum_accuracy,
            "version" : 1
           }
           ]
      }     
      
modelostr = json.dumps(modelo) #convertendo arquivo em str pra exibicao
modelo = json.loads(modelostr) #transformando a string em estrutura de dados Python

with open('teste.json', 'w') as f:
      json.dump(modelo, f)

with open('teste.json', 'r') as f:
      modelo = json.load(f)