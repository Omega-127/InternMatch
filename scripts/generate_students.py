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

#skills sampling

def sample_skills(min_skills=2, max_skills=5):
    skills = list(skills_pool.keys())
    weights = list(skills_pool.values())

    n = random.randint(min_skills, max_skills)
    chosen = np.random.choice(skills, size=n, replace=False, p=np.array(weights) / sum(weights))

    return sorted(chosen)

# required stipend

def stipend_range(cgpa: float):
    if cgpa >= 9.0:
        return (60000, 200000)
    elif cgpa >= 8.0:
        return (50000, 150000)
    elif cgpa >= 7.0:
        return (40000, 100000)
    else:
        return (30000, 70000)

# student generation

def generate_students(n: int = 200) -> pd.DataFrame:
    students = []

    for i in range(1, n+1):
        cgpa = round(random.gauss(7.8, 0.9), 2) # Mean 7.8, std 0.9
        cgpa = max(5.0, min(10.0, cgpa))    # Clamp to valid range

        batch_year = random.choices(years, weight=[0.15, 0.35, 0.15], k=1)[0]

        skills = sample_skills()

        location = random.choice(locations, weights=[0.30, 0.15, 0.15, 0.15, 0.10, 0.05, 0.05, 0.05], k=1)[0]

        stip_min, stip_max = stipend_range(cgpa)

        students.append({
            "student_id": i,
            "name": f"Student_{i}",
            "university": random.choice(universities),
            "degree": random.choice(degree),
            "batch_year": batch_year,
            "cgpa": cgpa,
            "skills": "|".join(skills),
            "domain_interest": random.choice(domains),
            "location": location,
            "willing_to_relocate": random.choice([True, False]),
            "internship_duration_months": random.choice([2, 3, 6]),
            "expected_stipend_min": stip_min,
            "expected_stipend_max": stip_max
        })

    return pd.DataFrame(students)

def validate(df: pd.DataFrame) -> bool:
    issues = []

    if df.isnull().any().any():
        issues.append("Found null values")
    if df['student_id'].nunique() != len(df):
        issues.append("Duplicate student ID")
    if(df['expected_stipend_min'] >= df['expected_stipend_max']).any():
        issues.append("stipend_min >= stipend_max")
    if(df['cgpa'] < 5.0 | df["cgpa"] > 10.0).any():
        issues.append("CGPA out of range")

    if issues:
        for issue in issues:
            print(issue)
        return False
    return True

def main():
    n = 200

    print(f"Generating {n} student profiles...")

    df = generate_students(n)

    print("Running validation...")
    if not validate(df):
        print("Validation failed. Fix issues before proceeding...")
        exit(1)

    os.makedirs("data", exist_ok=True)
    output_path = "data/students.csv"
    df.to_csv(output_path, index=False)

    print()
    print("  STUDENT DATA GENERATED SUCCESSFULLY")
    print(f"  Rows:            {len(df)}")
    print(f"  Output:          {output_path}")
    print(f"  Locations:       {df['location'].nunique()} unique")
    print(f"  Universities:    {df['university'].nunique()} unique")
    print(f"  Avg CGPA:        {df['cgpa'].mean():.2f}")
    print(f"  Top skills:")

    all_skills = [s for row in df['skills'] for s in row.split("|")]
    top_skills = pd.Series(all_skills).value_counts().head(5)


    for skill, count in top_skills.items():
        print(f"{skill:<22} {count} students")

    print()
    print("Next: run scripts/scrape_internshala.py")

if __name__ == "__main__":
    main()