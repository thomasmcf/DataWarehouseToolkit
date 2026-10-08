import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\thmcf\Documents\Programming\DataWarehouseToolkit\Chapter1")

cashier = pd.read_csv("DimCashier.csv")
date = pd.read_csv("DimDate.csv")
product = pd.read_csv("DimProduct.csv")
promotion = pd.read_csv("DimPromotion.csv")
store = pd.read_csv("DimStore.csv")

sale_dates = date.query("Year == 2025")["DateKey"].to_list()

for date in sale_dates:
    sale_count = np.random.poisson(1)

    if sale_count == 0:
        continue

    for day_sale in range(0, sale_count):
        # TODO

    
