from apscheduler.schedulers.background import BackgroundScheduler
from jobs import yearly, quarterly, monthly, weekly, daily, hourly, realtime #I created these 
#do I want to import tradable tickers? 

def schedule_scraping_jobs():
    scheduler = BackgroundScheduler()

    # Yearly (once per year, Jan 2nd)
    scheduler.add_job(yearly.run, 'cron', month='1', day='2', hour='1')

    # Quarterly (every 3 months, 1st day)
    scheduler.add_job(quarterly.run, 'cron', month='1,4,7,10', day='1', hour='1')

    # Monthly (1st of every month)
    scheduler.add_job(monthly.run, 'cron', day='1', hour='2')

    # Weekly (Sunday at 4am)
    scheduler.add_job(weekly.run, 'cron', day_of_week='sun', hour='4')

    # Daily (EOD scraping at 5pm)
    scheduler.add_job(daily.run, 'cron', hour='17')

    # Hourly (market hours, 9:30 AM to 4 PM)
    for hour in range(9, 16):
        scheduler.add_job(hourly.run, 'cron', hour=hour)
    #can do this alone:
    #scheduler.add_job(hourly.run, 'cron', minute=0)


    # Realtime scraping (every 10 mins during market hours)
    scheduler.add_job(realtime.run, 'cron', hour='9-16', minute='*/10')

    scheduler.start()

"""
example of incremental scraping 

# Weekly job

last_scraped = get_last_scraped_date_from_db_or_file(ticker, form_type, frequency)

if last_scraped is None: #the first time I'm running scraper, this will be none 
    print("First time scraping — using default start date")
    last_scraped = get_default_start_date(frequency) -- need to write, see below 

new_data = get_new_filings_since(ticker, last_scraped, form_type=form_type, frequency=frequency)
store_to_db(new_data) -- need to write from scratch 
update_last_scraped_date("AAPL", "10-K", "weekly", new_data["filedAt"].max()) -- need to write from scratch 

"""
from jobs.weekly import run_weekly_scraper

def schedule_jobs():
    run_weekly_scraper("AAPL", "10-K") #this means I'll have to 
