def tempKelvinToCelcius(value):
    '''
    Mengubah Kelvin ke Celcius dengan mengurangi suhu dengan 273.15
    :param value: Suhu dalam Kelvim | int or float

    :return: Suhu dalam Celcius | int or float
    '''
    return value - 273.15           # Mengubah Kelvin ke Celcius dengan mengurangi suhu dengan 273.15

def tempCelciusToKelvin(value):
    '''
    Mengubah Celcius ke Kelvin dengan menjumlahkan suhu dengan 273.15
    :param value: Suhu dalam Celcius | int or float

    :return: Suhu dalam Kelvin | int or float
    '''
    return value + 273.15           # Mengubah Celcius ke Kelvin dengan menambahkan suhu dengan 273.15

def tempToFahrenheit(value, isCorK = 'c'):
    '''
    Mengubah temperatur ke Fahrenheit
    :param value: Input suhu | int or float
    :param isCorK: Penanda apakah input suhu adalah Celcius atau Kelvin | str

    :return: Suhu dalam fahrenheit | int or float
    '''
    cases = ['c', 'k']              # Array yang berisi value apa saja yang boleh di taruh pada argument 'isCorK'

    if isCorK not in cases:         # Memeriksa apakah value argument isCorK terdapat pada array value yang kita tetapkan
        return None                     # Jika tidak ada, function berhenti disini dan return None

    if isCorK == 'k':                       # Memeriksa apakah isCorK merupakan 'k' (Suhu yang diberikan dalam Kelvin)
        value = tempKelvinToCelcius(value)      # Jika 'k', maka ubah suhu menjadi satuan Celcius
    return (value * 9 / 5) + 32             # Me-return value yang telah diubah dari Celcius ke Fahrenheit

def fahrenheitToTemp(value, isCorK = 'c'):
    '''
    Mengubah Fahrenheit ke suhu lain
    :param value: Input suhu dalam fahrenheit | int or float
    :param isCorK: Penanda apakah output suhu dalam Celcius atau Kelvin | str

    :return: Suhu dalam satuan yang telah di-specified | int or float
    '''
    cases = ['c', 'k']              # Array yang berisi value apa saja yang boleh di taruh pada argument 'isCorK'

    if isCorK not in cases:         # Memeriksa apakah value argument isCorK terdapat pada array value yang kita tetapkan
        return None                     # Jika tidak ada, function berhenti disini dan return None

    res = (value - 32) * 5 / 9      # Mengubah suhu dari Fahrenheit ke Celcius

    if isCorK == 'k':                   # Memeriksa apakah isCorK merupakan 'k' (Output suhu yang diminta adalah Kelvin)
        res = tempCelciusToKelvin(res)      # Jika 'k', maka ubah suhu menjadi satuan Kelvin
    return res                          # Return hasil akhir

print("Test K to C")
print("Input\t: 300 Kelvin")
print(f"Output\t: {round(tempKelvinToCelcius(300), 2)}")
print("==============================")

print("Test C to K")
print("Input\t: 100 Celcius")
print(f"Output\t: {round(tempCelciusToKelvin(100), 2)}")
print("==============================")

print("Test F to K")
print("Input\t: 100 Fahrenheit")
print(f"Output\t: {round(fahrenheitToTemp(100, 'k'), 2)}")
print("==============================")

print("Test F to C")
print("Input\t: 100 Fahrenheit")
print(f"Output\t: {round(fahrenheitToTemp(100, 'c'), 2)}")
print("==============================")

print("Test K to F")
print("Input\t: 100 Kelvin")
print(f"Output\t: {round(tempToFahrenheit(100, 'k'), 2)}")
print("==============================")

print("Test C to F")
print("Input\t: 100 Celcius")
print(f"Output\t: {round(tempToFahrenheit(100, 'c'), 2)}")
print("==============================")