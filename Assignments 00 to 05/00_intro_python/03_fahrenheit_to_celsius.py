#       ** 00_intro_python **

# 03_fahrenheit_to_celsius
def temp():
    print("Farenheit to Celcius: ")
    farenheit = float(input("Enter your farenheit degree. "))
    celsius = (farenheit - 32) * 5.0 / 9.0
    print(f"Temperature {farenheit} F = {celsius} C")
    

if __name__ == '__main__':
    temp()