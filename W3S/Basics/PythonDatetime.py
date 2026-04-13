# ==========================================
# Python Datetime
# ==========================================


# ------------------------------------------------
# Import Datetime Module
# ------------------------------------------------
import datetime


# ------------------------------------------------
# Current Date and Time
# datetime.datetime.now() returns current date & time
# ------------------------------------------------
now = datetime.datetime.now()
print("Now:", now)


# ------------------------------------------------
# Access Date Components
# ------------------------------------------------
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


# ------------------------------------------------
# Create a Specific Date
# datetime(year, month, day, hour, minute, second)
# ------------------------------------------------
specific_date = datetime.datetime(2025, 1, 1, 12, 0, 0)
print("Specific date:", specific_date)


# ------------------------------------------------
# Date Object (without time)
# ------------------------------------------------
today = datetime.date.today()
print("Today:", today)


# ------------------------------------------------
# Time Object
# ------------------------------------------------
current_time = datetime.datetime.now().time()
print("Current time:", current_time)


# ------------------------------------------------
# strftime() - Format Date/Time
# Converts datetime to formatted string
# ------------------------------------------------
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)


# Common format codes:
# %Y → Year (2025)
# %m → Month (01-12)
# %d → Day (01-31)
# %H → Hour (00-23)
# %M → Minute
# %S → Second
# %A → Weekday name
# %B → Month name


# ------------------------------------------------
# strptime() - Parse String to Datetime
# ------------------------------------------------
date_str = "2025-12-31"
parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed:", parsed)


# ------------------------------------------------
# timedelta
# Used for date arithmetic
# ------------------------------------------------
delta = datetime.timedelta(days=5)
future = now + delta
past = now - delta

print("Future:", future)
print("Past:", past)


# ------------------------------------------------
# Difference Between Dates
# ------------------------------------------------
date1 = datetime.datetime(2025, 1, 1)
date2 = datetime.datetime(2025, 1, 10)

difference = date2 - date1
print("Difference (days):", difference.days)


# ------------------------------------------------
# Replace Date/Time Values
# ------------------------------------------------
modified = now.replace(year=2030, month=12)
print("Modified:", modified)


# ------------------------------------------------
# Timezone (Basic Usage)
# ------------------------------------------------
utc_now = datetime.datetime.utcnow()
print("UTC Now:", utc_now)


# ------------------------------------------------
# When to Use Datetime
# - Logging timestamps
# - Scheduling tasks
# - Calculating durations
# - Formatting dates for display
# ------------------------------------------------