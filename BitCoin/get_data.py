import yfinance as yf
import pandas as pd
import openpyxl

btc_data = yf.download('BTC-USD', start='2020-01-01', end='2025-02-26')
btc_data.to_excel('BitCoin\data_ema.xlsx', sheet_name='data_ema')