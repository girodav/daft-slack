# Edit your search criteria in this file.

from daftlistings import RentType, SortOrder, SortType
import logging

# Logging module configuration

LOG_LEVEL = logging.INFO

# The Slack Webhook URL. Create an application here: https://api.slack.com/apps?new_app=1
SLACK_URL = '<WEBHOOK URL>'
SLACK_URL_ERRORS = '<ERROR_URL>'

# The information to send to the estate agent/landlord as part of your message
NAME = '<my name>'
EMAIL = '<my email>'
PHONE_NUMBER = '<my phone number>'
MESSAGE = '<my message>'

# Database path and name
DB_PATH = 'daft.db'

# The listings you'd like to scrape i.e houses, properties, auction, commercial or apartments.
# Use the SaleType or RentType enum to select the listing type.
LISTING_TYPE = RentType.ANY

MIN_BEDS = 1

# What Daft.ie areas to search on.
# Example
# COUNTY = "Dublin City"
# AREAS = ["Dublin 4", "Dublin 6", "Dublin 6w", "Dublin 12", "Dublin 14", "Dublin 15", "Dublin 16", "Dublin 18",
#          'Dublin 20']
COUNTY = "Dublin City"
AREAS = [""]

# Set this to retrieve ads that are a given number of days old.
# For example to retrieve listings that have been been added a week ago: ADDED_SINCE = 7
ADDED_SINCE = 7

# Set to 'True' to only get rental properties that are furnished.
FURNISHED = 'True'

# Use the SortOrder object to sort the listings descending or ascending.
# Example: SortOrder.DESCENDING
SORT_ORDER = SortOrder.DESCENDING

# Use this setting to sort by price, distance, upcoming viewing or date using the SortType object.
# example SortType.DATE
SORT_BY = SortType.DATE

# Set to 'True' to only get listings that has photos.
WITH_PHOTOS = 'True'

# Minimum lease period, in months
MIN_LEASE = 12

# The minimum rent you want to pay per month.
MIN_PRICE = 0

# The maximum rent you want to pay per month.
MAX_PRICE = 9999
