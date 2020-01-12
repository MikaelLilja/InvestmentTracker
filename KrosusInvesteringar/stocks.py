from enum import Enum
from collections import namedtuple

class Stock():
   def __init__(self, name, code, isin):
       self.name = name
       self.code = code
       self.isin = isin

class Stocks():
    Ericsson =      Stock('Ericsson A', 'ERIC A', 'SE0000108649')
    NovoNordisk =   Stock('Novo Nordisk B', 'NOVO B', 'DK0060534915')
    DnbTeknologi =  Stock('DNB Teknologi A', '?', 'NO0010337678')
    UsaIndex =      Stock('Handelsbanken USA Ind Crit A1 SEK', '?', 'SE0004139780')
    SmaBolagIndex = Stock('PLUS Smabolag Sverige Index', '?', 'SE0010323642')
    SebBioTek =     Stock('SEB Bioteknikfond C EUR - Lux', '?', 'LU0385485148')
    RoburAsien =    Stock('Swedbank Robur Access Asien', '?', 'SE0007074117')

def getTransactions():
    transactions = []
    transactions.append([6218, '2019-12-03', Stocks.SmaBolagIndex])
    # transacations.append([-19,      '2019-08-21', 'Utländsk källskatt'])
    # transacations.append([69,   '2019-08-21', 'UTDELNING - Novo Nordisk B'])
    # transacations.append([82, '2019-04-02', 'UTDELNING - Ericsson A'])
    # transacations.append([-30,98, '2019-03-26', 'Utländsk källskatt'])
    # transacations.append([114,74, '2019-03-26', 'UTDELNING - Novo Nordisk B'])
    transactions.append([300,  '2018-10-25', Stocks.SebBioTek])
    transactions.append([422,  '2018-10-24', Stocks.RoburAsien])
    transactions.append([300,  '2018-10-24', Stocks.DnbTeknologi])
    transactions.append([300,  '2018-10-23', Stocks.UsaIndex])
    transactions.append([390,  '2018-10-22', Stocks.NovoNordisk])
    transactions.append([338,  '2018-10-22', Stocks.Ericsson])
    transactions.append([6200, '2018-10-12', Stocks.RoburAsien])
    transactions.append([650,  '2018-10-11', Stocks.DnbTeknologi])
    transactions.append([1500, '2018-10-11', Stocks.SebBioTek])
    transactions.append([5869, '2018-10-10', Stocks.NovoNordisk])
    transactions.append([6240, '2018-10-10', Stocks.Ericsson])
    transactions.append([6200, '2018-10-09', Stocks.UsaIndex])
    transactions.append([4027, '2017-04-27', Stocks.SebBioTek])
    transactions.append([4000, '2017-04-26', Stocks.DnbTeknologi])
    return transactions