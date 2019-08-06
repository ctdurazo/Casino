

def generate_number(min, max):
    import random 
    the_number = random.randint(min, max)
    if the_number == 37:
        number = "00"
    else:
        number = str(the_number)
    return number

def isEvenOrOdd(number_string):
    number_int = int(number_string)
    if number_int == 0:
        return "neither"
    elif number_int % 2 == 0:
        return "even"
    else:
        return "odd"

def getColor(number_string):
    if number_string in ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]:
        color = "red"
    if number_string in ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]:
        color = "black"
    if number_string in ["0", "00"]:
        color = "green"
    return color
