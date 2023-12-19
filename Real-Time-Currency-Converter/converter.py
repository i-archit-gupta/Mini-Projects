from forex_python.converter import CurrencyRates
curr = CurrencyRates()
amt = int(input("Enter the amount: "))
from_curr = input("From Currency: ").upper()
to_curr = input("To Currency: ").upper()
print(from_curr, " To ", to_curr, amt)
result = curr.convert(from_curr, to_curr, amt)
print(result)
