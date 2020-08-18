temperaturas_celsius = [22.5, 40, 13, 29, 34]
temperaturas_fahrenheit = list(map(lambda temp: round((9 / 5) * temp + 32, 1), temperaturas_celsius))
print(temperaturas_fahrenheit)