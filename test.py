def convert_to_float_or_str(value):
    try:
        result = float(value)
        return result
    except:
        return value
proverka = convert_to_float_or_str('  1   5 '.strip().replace(" ", ""))
print(proverka)