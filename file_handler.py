
def read_file(filename):
    try: 
        with open(filename,'r', encoding='utf = 8') as file:
            text = file.read()

        return text
    except FileNotFoundError:
        print('Error!..File not found')
        return ""

