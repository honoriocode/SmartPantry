#Items duration at home
import pandas as pd
from openpyxl import load_workbook
import datetime
import time
import os

#honoriocode_contribution
#new dataframe

df = pd.DataFrame(columns =['Name', 'Price', 'Quantity', 'Date'])

#new excel file 

file = 'ProductDuration.xlsx'


print("Enter 'no' for product to end the program\n")

#asking for input then appending to dataframe 

while True:

    product = input("Product: ").lower()
    if product == 'no':
        print('Til next time! Bye.')
        break
    current_price = float(input("Price: "))
    date = input("Bought on: ")
    quantity = int(input('Enter quantity: '))

    data = {'Name': product, 'Price': current_price, 'Quantity': quantity, 'Date': date}
    
    df.loc[len(df)] = data
    df.to_excel('ProductDuration.xlsx', index = False)
