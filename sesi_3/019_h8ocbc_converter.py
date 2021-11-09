### SOAL 1 ###
def convertKelvinCelcius(value, isCtoK=True):
    '''
    Mengconvert temperatur (Kelvin ke Celcius, dan sebaliknya)
    :param value: Input suhu | int or float
    :param isCtoK: Penanda apakah input suhu adalah Celcius atau Kelvin | boolean

    :return: Suhu dalam fahrenheit | int or float
    '''
    if isCtoK:
        return tempCelciusToKelvin(value)
    else:
        return tempKelvinToCelcius(value)

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

### SOAL 2 ###
def tempToFahrenheit(value, CorK = 'c'):
    '''
    Mengubah temperatur ke Fahrenheit
    :param value: Input suhu | int or float
    :param CorK: Penanda apakah input suhu adalah Celcius atau Kelvin | str

    :return: Suhu dalam fahrenheit | int or float
    '''
    cases = ['c', 'k']              # Array yang berisi value apa saja yang boleh di taruh pada argument 'CorK'

    if CorK not in cases:         # Memeriksa apakah value argument CorK terdapat pada array value yang kita tetapkan
        return None                     # Jika tidak ada, function berhenti disini dan return None

    if CorK == 'k':                       # Memeriksa apakah CorK merupakan 'k' (Suhu yang diberikan dalam Kelvin)
        value = tempKelvinToCelcius(value)      # Jika 'k', maka ubah suhu menjadi satuan Celcius
    return (value * 9 / 5) + 32             # Me-return value yang telah diubah dari Celcius ke Fahrenheit

### SOAL 3 ###
def fahrenheitToTemp(value, CorK = 'c'):
    '''
    Mengubah Fahrenheit ke suhu lain
    :param value: Input suhu dalam fahrenheit | int or float
    :param CorK: Penanda apakah output suhu dalam Celcius atau Kelvin | str

    :return: Suhu dalam satuan yang telah di-specified | int or float
    '''
    cases = ['c', 'k']              # Array yang berisi value apa saja yang boleh di taruh pada argument 'CorK'

    if CorK not in cases:         # Memeriksa apakah value argument CorK terdapat pada array value yang kita tetapkan
        return None                     # Jika tidak ada, function berhenti disini dan return None

    res = (value - 32) * 5 / 9      # Mengubah suhu dari Fahrenheit ke Celcius

    if CorK == 'k':                   # Memeriksa apakah CorK merupakan 'k' (Output suhu yang diminta adalah Kelvin)
        res = tempCelciusToKelvin(res)      # Jika 'k', maka ubah suhu menjadi satuan Kelvin
    return res                          # Return hasil akhir

def getUserInput(prompt):
    '''
    Mengambil input angka dari user
    :param prompt: Text yang ingin ditampilkan saat meminta input | string

    :return: Nilai float yang telah di-parse dari input user | float
    '''
    done = False

    while(not done):
        print(prompt, end="")
        try:
            val = float(input())
        except ValueError:
            print("Must be a number!\n")
        else:
            done = True

    return val

print("==============================")
print("Test K to C")
val = getUserInput("Input (Kelvin)\t: ")
print(f"Output\t\t: {round(convertKelvinCelcius(val, isCtoK=False), 2)}")
print("==============================")

print("Test C to K")
val = getUserInput("Input (Celcius)\t: ")
print(f"Output\t\t: {round(convertKelvinCelcius(val, isCtoK=True), 2)}")
print("==============================")

print("Test F to K")
val = getUserInput("Input (Fahrnt.)\t: ")
print(f"Output\t\t: {round(fahrenheitToTemp(val, 'k'), 2)}")
print("==============================")

print("Test F to C")
val = getUserInput("Input (Fahrnt.)\t: ")
print(f"Output\t\t: {round(fahrenheitToTemp(val, 'c'), 2)}")
print("==============================")

print("Test K to F")
val = getUserInput("Input (Kelvin)\t: ")
print(f"Output\t\t: {round(tempToFahrenheit(val, 'k'), 2)}")
print("==============================")

print("Test C to F")
val = getUserInput("Input (Celcius)\t: ")
print(f"Output\t\t: {round(tempToFahrenheit(val, 'c'), 2)}")
print("==============================")