#creating the files in the directory
'''
New-Item jobs\yearly.py -ItemType File
New-Item jobs\quarterly.py -ItemType File
New-Item jobs\monthly.py -ItemType File
New-Item jobs\weekly.py -ItemType File
New-Item jobs\daily.py -ItemType File
New-Item jobs\hourly.py -ItemType File
New-Item jobs\realtime.py -ItemType File
New-Item main.py -ItemType File
New-Item scheduler.py -ItemType File

'''

#creating a virtual environment
# python -m venv venv

#isnteall project dependecies 
#pip install fastapi uvicorn apscheduler yfinance requests

#freeze the libraries in their exact version
#pip freeze > requirements.txt --do this after any major installs 

#reintering/activating virtual evironment 
#rectivate scripts - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#go to the venv path --  venv\Scripts\Activate.ps1

#installed
#pip install requests-html lxml_html_clean
#pip install pandas==1.1.5 numpy==1.19.4 scipy==1.5.4
#pip3 install alpaca-trade-api --- april 12th, won't need it anymore 

#setting up an .env file 
#pip install python-dotenv
#create .env file in the root of the directory -- will use the .env file in all scraping files
        #using from dotenv import load_dotenv
#click on add file in vscode in the left side menue

''' #delete this, it was only for testing 
from alpaca.data.live import StockDataStream
from alpaca.data.requests import StockLatestTradeRequest
from alpaca.data.historical import StockHistoricalDataClient
import requests

cl = StockHistoricalDataClient(
    api_key="PKQ339A898RGXEO6NK9F",
    secret_key="u1IFlQhrUy097zSB7zOa2LGDxeO2GRia3yCP0aK7"
)

# Create the request
request_new = StockLatestTradeRequest(symbol_or_symbols="AAPL") #the function changed

# Fetch the latest trade
trade = cl.get_stock_latest_trade(request_new)

print(trade)

'''