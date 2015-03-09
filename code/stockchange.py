"""
Program for computing and visualizing the daily 
percentage changes of major stocks. The data is 
obtained via yahoo
"""
import numpy as np
import pandas as pd
import datetime as dt
import pandas.io.data as web
import matplotlib.pyplot as plt

#set period
start, end = dt.datetime(2014, 2, 1), dt.datetime(2015, 2, 1)

ticker_values = {"INTC": "Intel",
               "MSFT": "Microsoft",
               "IBM": "IBM",
               "BHP": "BHP",
               "RSH": "RSH",
               "TM": "Toyota",
               "AAPL": "Apple",
               "AMZN": "Amazon",
               "BA": "Boing",
               "QCOM": "Qualcomm",
               "KO": "Coca-Cola",
               "GOOG": "Google",
               "SNE": "Sony",
               "PTR": "PetroChina"}

stocks = ticker_list.keys()
percentage_data = pd.DataFrame()

# pull data and compute percentage change
for entry in range(1,len(stocks)):
    data = web.DataReader(stocks[entry], "yahoo", start, end)
    temp = np.diff(data["Adj Close"])
    data = data.ix[1:,]
    data["perchange"] = temp
    percentage_data[stocks[entry]] = data["perchange"]

# Visualize
plt.plot(percentage_data)
legend(percentage_data.columns)
plt.show()


