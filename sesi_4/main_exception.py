import sys

def customExc():
    x = 10
    if x > 5:
        raise Exception(f'Salah X nya tuh! X-nya ({x})')

def assertExc(os="win32"):
    assert(os in sys.platform), f"This code runs on {os} only"

    print("No exception raised!")

def tryCatchExc(os):
    try:
        assertExc(os)
    except Exception as e:
        print("Inside except in tryCatchExc()")
        print(e)
        pass

def fileOpenExc():
    try:
        assertExc("linux")
        with open('data/file.log') as f:
            read_data = f.read()
    except FileNotFoundError as fnf_err:
        print(fnf_err)
    except AssertionError as err:
        print(err)
        print("assertExc() was not executed")

def tryCatchElseFinally():
    try:
        assertExc()
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('Cleaning up, irrespective of any exceptions.')

# customExc()

# assertExc()

# tryCatchExc('linux')
# print('\n')
# tryCatchExc('win32')

# fileOpenExc()

tryCatchElseFinally()

print("Program berhasil selesai!")