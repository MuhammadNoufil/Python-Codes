
#Unit Converter

def length_converter():
    print("Length Converter")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Mile to Kilometer")
    print("4. Kilometer to Mile")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        km = float(input("Enter value in Kilometer: "))
        m = km * 1000
        print(f"{km} Kilometer is equal to {m} Meter")
        
    elif choice == 2:
        m = float(input("Enter value in Meter: "))
        km = m / 1000
        print(f"{m} Meter is equal to {km} Kilometer")
        
    elif choice == 3:
        mile = float(input("Enter value in Mile: "))
        km = mile * 1.60934
        print(f"{mile} Mile is equal to {km} Kilometer")
        
    elif choice == 4:
        km = float(input("Enter value in Kilometer: "))
        mile = km / 1.60934
        print(f"{km} Kilometer is equal to {mile} Mile")
        
    else:
        print("Invalid choice")

def weight_converter():
    print("Weight Converter")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Pound to Kilogram")
    print("4. Kilogram to Pound")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        kg = float(input("Enter value in Kilogram: "))
        g = kg * 1000
        print(f"{kg} Kilogram is equal to {g} Gram")
        
    elif choice == 2:
        g = float(input("Enter value in Gram: "))
        kg = g / 1000
        print(f"{g} Gram is equal to {kg} Kilogram")
        
    elif choice == 3:
        pound = float(input("Enter value in Pound: "))
        kg = pound / 2.20462
        print(f"{pound} Pound is equal to {kg} Kilogram")
        
    elif choice == 4:
        kg = float(input("Enter value in Kilogram: "))
        pound = kg * 2.20462
        print(f"{kg} Kilogram is equal to {pound} Pound")
        
    else:
        print("Invalid choice")

def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        c = float(input("Enter value in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c} Celsius is equal to {f} Fahrenheit")
        
    elif choice == 2:
        f = float(input("Enter value in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f} Fahrenheit is equal to {c} Celsius")
        
    else:
        print("Invalid choice")

def main():
    print("Unit Converter")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        length_converter()
    elif choice == 2:
        weight_converter()
    elif choice == 3:
        temperature_converter()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
