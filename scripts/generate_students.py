import numpy as np
import pandas as pd
import random
import os

random.seed(42)
np.random.seed(42)

skills_pool = {
    "Python": 0.70,
    "Java": 0.55,
    "Javascript": 0.60,
    "C++": 0.35,
    "React": 0.45,
    "Node.js": 0.40,
    "Django": 0.35,
    "FastAPI": 0.25,
    "Spring Boot": 0.30,
    "Machine Learning": 0.40,
    "Data Science": 0.35,
    "SQL": 0.55,
    "PostgreSQL": 0.30,
    "MongoDB": 0.30,
    "AWS": 0.30,
    "Docker": 0.25,
    "Git": 0.65,
    "REST APIs": 0.45,
    "TypeScript": 0.30,
    "Flutter": 0.20
}

domains = [
    "fintech",
    "healthcare",
    "ecommerce",
    "infra",
    "SaaS",
    "media"
]

locations = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Pune",
    "Hyderabad",
    "Chennai",
    "kolkata",
    "Remote"
]

universities = [
    "BITS Pilani",
    "IIT Bombay",
    "IIT Delhi",
    "IIT Madras",
    "IIIT Bangalore",
    "NIT Trichy",
    "NIT Suratkal",
    "VIT Vellore",
    "DTU Delhi",
    "Symbiosis Pune",
    "COEP Pune",
    "Amity University",
    "SRM University",
    "Manipal Institute of Technology",
    "VJTI Mumbai"
]

degree = [
    "B.Tech Computer Science",
    "B.Tech Information Technology",
    "B.Tech Electronics and Telecommunication",
    "B.E. Computer Engineering",
    "B.Sc. Computer Science",
    "B.Tech Artificial Intelligence",
    "B.Tech Data Science",
    "BCA",
    "MCA",
    "M.Tech Computer Science"
]

years = [2026, 2027, 2028, 2029]