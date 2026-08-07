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

domain_map = {
    "finance":          "fintech",
    "banking":          "fintech",
    "fintech":          "fintech",
    "health":           "healthcare",
    "medical":          "healthcare",
    "pharma":           "healthcare",
    "ecommerce":        "ecommerce",
    "retail":           "ecommerce",
    "shopping":         "ecommerce",
    "education":        "edtech",
    "teaching":         "edtech",
    "e-learning":       "edtech",
    "cloud":            "infra",
    "devops":           "infra",
    "infrastructure":   "infra",
    "media":            "media",
    "content":          "media",
    "marketing":        "media",
    "software":         "SaaS",
    "saas":             "SaaS",
    "technology":       "SaaS",
}

known_skills = [
    "Python", "Java", "JavaScript", "C++", "React", "Node.js",
    "Django", "FastAPI", "Spring Boot", "Machine Learning",
    "Data Science", "SQL", "PostgreSQL", "MongoDB", "AWS",
    "Docker", "Git", "REST APIs", "TypeScript", "Flutter",
    "Kotlin", "Swift", "Go", "Rust", "TensorFlow", "PyTorch",
    "Pandas", "NumPy", "Excel", "Power BI", "Tableau",
]

