
PESO_RATE = 57.17
YEN_RATE = 146.67


def convert_currency(dollar_list):
    results = []
    for dollar in dollar_list:
        peso = dollar * PESO_RATE
        yen = dollar * YEN_RATE
        results.append((dollar, peso, yen))  
    return results


raw_input = input("Enter currency in ($): ")

parts = raw_input.replace(" ", "").split(",")

dollar_values = [float(p) for p in parts]

converted = convert_currency(dollar_values)


print("\nDollar($)\tPhil Peso(P)\tJpn Yen (Y)")
for d, p, y in converted:
    print(f"{d:.2f}\t\t{p:.2f}\t\t{y:.2f}")