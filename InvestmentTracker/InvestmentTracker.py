# from stocks import Stocks, getTransactions
from morningstar.morningstar_client import MorningstarClient
client = MorningstarClient()

instrument = ''
startDate = ''
endDate = ''
bar_type = 'dailybar'

client.get_instrument_prices(instrument='28.10.F00000JQA9', start_date='01-01-2019', end_date='02-01-2019')
client.provider.search({'isin': "CH0038863350"})

print('hej')

ourTransactions = getTransactions()
