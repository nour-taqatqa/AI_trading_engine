from fastapi import FastAPI
from scheduler import schedule_scraping_jobs

app = FastAPI()

@app.on_event("startup")
def startup_event():
    schedule_scraping_jobs()

"""
we’re referring to the moment the FastAPI server is launched, not when someone visits it in a browser.

when the server spins up, it'll kick off your scraping scheduler immediately — even if no one visits the API.
"""

#do I need the following:
"""
from fastapi import FastAPI, BackgroundTasks
from scheduler import schedule_scraping_jobs
from scraper import yahoo, alpaca, sec

app = FastAPI()

# Initialize scheduled scraping jobs
schedule_scraping_jobs()

@app.get("/")
def root():
    return {"message": "Financial Data Scraper API is running."}

@app.get("/scrape/ticker/{ticker}")
def scrape_single_ticker(ticker: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(yahoo.scrape_all_yahoo, ticker)
    background_tasks.add_task(alpaca.scrape_all_alpaca, ticker)
    background_tasks.add_task(sec.scrape_all_sec, ticker)
    return {"message": f"Scraping initiated for {ticker}"}

@app.get("/scrape/all")
def scrape_all(background_tasks: BackgroundTasks):
    # This could also be paginated or triggered in batches.
    tickers = yahoo.get_all_tickers()
    for ticker in tickers:
        background_tasks.add_task(yahoo.scrape_all_yahoo, ticker)
        background_tasks.add_task(alpaca.scrape_all_alpaca, ticker)
        background_tasks.add_task(sec.scrape_all_sec, ticker)
    return {"message": "Scraping initiated for all tickers."}

"""