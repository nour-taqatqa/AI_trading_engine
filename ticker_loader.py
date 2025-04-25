# ticker_loader.py
import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

load_dotenv()

def get_tradable_tickers(exchange_filter=None):
    api = tradeapi.REST(
        os.getenv("ALPACA_API_KEY"),
        os.getenv("ALPACA_SECRET_KEY"),
        base_url=os.getenv("ALPACA_BASE_URL")
    )

    assets = api.list_assets(status='active')
    tickers = [
        asset.symbol for asset in assets
        if asset.tradable and (exchange_filter is None or asset.exchange in exchange_filter)
    ] #check if it's tradable becasue some stocks dissapear in a day 
    #print(tickers)
    return tickers

#if __name__ == "__main__": -- it works 
#    tickers= get_tradable_tickers(exchange_filter=["NYSE", "NASDAQ"])
#    print(tickers[:10])  # print first 10 to verify it's working
