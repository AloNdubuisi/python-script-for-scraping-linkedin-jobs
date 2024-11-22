# Scrapy settings for linkedin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Scrapy settings for linkedin project

BOT_NAME = 'linkedin'

SPIDER_MODULES = ['linkedin.spiders']
NEWSPIDER_MODULE = 'linkedin.spiders'

# Disable robots.txt rules (set to False to ignore)
ROBOTSTXT_OBEY = False

# Default request headers to simulate a real browser request
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://www.linkedin.com/',
    'Connection': 'keep-alive',
}

# ScrapeOps configuration
SCRAPEOPS_API_KEY = 'fca7409b-112b-4704-80cd-9d4b84a58c8b'
SCRAPEOPS_PROXY_ENABLED = True

# Add ScrapeOps monitoring extension
EXTENSIONS = {
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
}

# Downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Retry settings
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [403, 429, 500, 502, 503, 504]

# Concurrency and request delay
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# Logging level
LOG_LEVEL = 'DEBUG'
