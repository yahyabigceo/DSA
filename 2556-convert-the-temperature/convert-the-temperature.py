class Solution(object):
    def convertTemperature(self, celsius):
       Kelvin = celsius + 273.15
       Fahrenheit = celsius * 1.80 + 32.00
       result=[Kelvin,Fahrenheit]
       return  result
      
        