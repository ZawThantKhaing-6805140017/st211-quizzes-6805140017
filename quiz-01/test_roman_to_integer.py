from roman_to_integer import convert

def test_convert():
    assert convert("III") == 3     
    assert convert("IV") == 4
    assert convert("VI") == 6
    assert convert("IX") == 9
    assert convert("LVIII") == 58
    assert convert("MCMXCIV") == 1994
    