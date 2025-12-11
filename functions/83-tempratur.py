# convert temperature from celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(30))

# convert temperature from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(fahrenheit_to_celsius(86))
