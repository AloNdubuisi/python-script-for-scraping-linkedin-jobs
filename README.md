# python-script-for-scraping-linkedin-jobs

Python Scrapy spiders that scrape job data & people and company profiles from [LinkedIn.com](https://www.linkedin.com/).

# What is needed

# First delete my own JSON file, its automatic so your own will be create.

## ScrapeOps Proxy

This LinkedIn spider uses [ScrapeOps Proxy](https://scrapeops.io/proxy-aggregator/) as the proxy solution. ScrapeOps has a free plan that allows you to make up to 1,000 requests per month which makes it ideal for the development phase, but can be easily scaled up to millions of pages per month if needs be.

You can [sign up for a free API key here](https://scrapeops.io/app/register/main).

To use the ScrapeOps Proxy you need to first install the proxy middleware:

```python

pip install scrapeops-scrapy-proxy-sdk

```

Then activate the ScrapeOps Proxy by adding your API key to the `SCRAPEOPS_API_KEY` in the `settings.py` file.

```python

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'  # This is the only thing you may have to edit and change here nased on your own API key

SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

```

## ScrapeOps Monitoring

To monitor the scraper, this spider uses the [ScrapeOps Monitor](https://scrapeops.io/monitoring-scheduling/), a free monitoring tool specifically designed for web scraping.

**Live demo here:** [ScrapeOps Demo](https://scrapeops.io/app/login/demo)

![ScrapeOps Dashboard](https://scrapeops.io/assets/images/scrapeops-promo-286a59166d9f41db1c195f619aa36a06.png)

To use the ScrapeOps Proxy you need to first install the monitoring SDK:

```

pip install scrapeops-scrapy

```

Then activate the ScrapeOps Proxy by adding your API key to the `SCRAPEOPS_API_KEY` in the `settings.py` file.

```python

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'   #Replace with your own API key

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
}


DOWNLOADER_MIDDLEWARES = {

    ## ScrapeOps Monitor
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,

    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

```

If you are using both the ScrapeOps Proxy & Monitoring then you just need to enter the API key once.

## Running The Scrapers

Make sure Scrapy and the ScrapeOps Monitor is installed:

```

pip install scrapy scrapeops-scrapy

```

Then to run the spider, enter one of the following command:

```

scrapy crawl linkedin_jobs

```

### Speeding Up The Crawl

The spiders are set to only use 1 concurrent thread in the `settings.py` file as the ScrapeOps Free Proxy Plan only gives you 1 concurrent thread.

However, if you upgrade to a paid ScrapeOps Proxy plan you will have more concurrent threads. Then you can increase the concurrency limit in your scraper by updating the `CONCURRENT_REQUESTS` value in your `settings.py` file.

```python
# settings.py

CONCURRENT_REQUESTS = 10

```

### Storing Data

custom*settings = {
'FEEDS': { 'data/%(name)s*%(time)s.csv': { 'format': 'csv',}}
}

````
# If you wish to save it as a JSON file, Run this command:

scrapy crawl linkedin_jobs -O jobs.json

#This will automaticall create a JSON file and save all the scrapped data.


If you would like to save your CSV files to a AWS S3 bucket then check out the [Saving CSV/JSON Files to Amazon AWS S3 Bucket guide here](https://scrapeops.io//python-scrapy-playbook/scrapy-save-aws-s3)

Or if you would like to save your data to another type of database then be sure to check out these guides:

- [Saving Data to JSON](https://scrapeops.io/python-scrapy-playbook/scrapy-save-json-files)
- [Saving Data to SQLite Database](https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-sqlite)
- [Saving Data to MySQL Database](https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-mysql)
- [Saving Data to Postgres Database](https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-postgres)

### Deactivating ScrapeOps Proxy & Monitor

To deactivate the ScrapeOps Proxy & Monitor simply comment out the follow code in your `settings.py` file:

```python
# settings.py

# SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

# SCRAPEOPS_PROXY_ENABLED = True

# EXTENSIONS = {
# 'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
# }

# DOWNLOADER_MIDDLEWARES = {

#     ## ScrapeOps Monitor
#     'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,

#     ## Proxy Middleware
#     'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
# }



````
