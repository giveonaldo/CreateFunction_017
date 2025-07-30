
def convert_temperature(value, unit):
    """
    Convert temperature between Celsius and Fahrenheit.
    :param value: numeric temperature value
    :param unit: 'C' for Celsius, 'F' for Fahrenheit
    :return: converted temperature value
    """
    if unit.upper() == 'C':
        # Celsius to Fahrenheit
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        # Fahrenheit to Celsius
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit must be 'C' or 'F'")

# Lambda function to calculate area of a circle
area_circle = lambda r: 3.141592653589793 * r * r

if __name__ == "__main__":
    # Temperature conversion
    value = float(input("Masukkan nilai suhu: "))
    unit = input("Masukkan satuan suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")
    try:
        converted = convert_temperature(value, unit)
        if unit.upper() == 'C':
            print(f"{value}°C = {converted:.2f}°F")
        elif unit.upper() == 'F':
            print(f"{value}°F = {converted:.2f}°C")
    except ValueError as e:
        print(e)

    # Area of a circle
    r = float(input("Masukkan jari-jari lingkaran: "))
    area = area_circle(r)
    print(f"Luas lingkaran dengan jari-jari {r} adalah {area:.2f}")
