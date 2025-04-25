from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

def get_default_start_date(frequency):
    today = date.today()
    if frequency == "yearly":
        return (today - relativedelta(years=10)).isoformat()
    elif frequency == "quarterly":
        return (today - relativedelta(years=5)).isoformat()
    elif frequency == "monthly":
        return (today - relativedelta(years=3)).isoformat()
    elif frequency == "weekly":
        return (today - relativedelta(years=1)).isoformat()
    else:
        raise ValueError("Invalid frequency")

def get_date_ranges(frequency, num_periods):
    today = datetime.today().date()
    ranges = []

    for i in range(num_periods):
        if frequency == 'yearly':
            end = today - relativedelta(years=i)
            start = end - relativedelta(years=1)
        elif frequency == 'quarterly':
            end = today - relativedelta(months=3 * i)
            start = end - relativedelta(months=3)
        elif frequency == 'monthly':
            end = today - relativedelta(months=i)
            start = end - relativedelta(months=1)
        elif frequency == 'weekly':
            end = today - timedelta(weeks=i)
            start = end - timedelta(weeks=1)
        else:
            raise ValueError("Invalid frequency")

        ranges.append((start.isoformat(), end.isoformat()))

    return ranges