import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import random
import os
import json

base_url = 'https://internshala.com/internships'

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebkit/537.36 (KHTML, like gecko)"
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US, en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}