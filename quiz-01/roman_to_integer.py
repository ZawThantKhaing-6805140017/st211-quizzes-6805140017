values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def convert(roman):
    total = 0
    for i in range(len(roman)): 
        if i+1 < len(roman) and values[roman[i]] < values[roman[i+1]]: #check if there is (a next character) and compare the values (if the current value is less than the next value,we will subtract the current value)
            total -= values[roman[i]]
        else:
            total += values[roman[i]]
    return total

roman = input("Enter a Roman numeral: ").upper()#put this line into comment when running pytest
print(f"The integer value of {roman} is {convert(roman)}")#put this line into comment when running pytest