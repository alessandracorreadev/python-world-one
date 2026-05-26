from ex112_package.utilities import currency
from ex112_package.utilities import data

user_input = data.read_price("Enter the price: $")
currency.analysis(user_input, 10, 20)