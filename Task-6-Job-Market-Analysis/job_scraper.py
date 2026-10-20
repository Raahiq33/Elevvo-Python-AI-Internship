
from pathlib import Path
from collections import Counter

import pandas as pd
from bs4 import BeautifulSoup


# Project files
BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "practice_jobs.html"
OUTPUT_FILE = BASE_DIR / "job_listings.csv"
SKILLS_FILE = BASE_DIR / "top_skills.csv"


def extract_jobs():
    """Extract job listings from the local practice HTML file."""

    if not HTML_FILE.exists():
        print("Error: practice_jobs.html not found!")
        return []

    html = HTML_FILE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    for card in soup.select("article.job-card"):
        title = card.select_one(".job-title")
        company = card.select_one(".company")
        location = card.select_one(".location")
        date = card.select_one("time")

        skills = [
            skill.get_text(strip=True)
            for skill in card.select(".skill")
        ]

        job = {
            "Job Title": title.get_text(strip=True) if title else "",
            "Company": company.get_text(strip=True) if company else "",
            "Location": location.get_text(strip=True) if location else "",
            "Skills": ", ".join(skills),
            "Posted Date": date.get("datetime", "") if date else ""
        }

        jobs.append(job)

    return jobs


def analyze_jobs(jobs):
    """Clean job data and analyze skills and job roles."""

    if not jobs:
        print("No job listings found.")
        return

    df = pd.DataFrame(jobs)

    # Data cleaning
    df = df.drop_duplicates()
    df = df.dropna(subset=["Job Title", "Company"])
    df["Posted Date"] = pd.to_datetime(
        df["Posted Date"], errors="coerce"
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("\n===== JOB MARKET ANALYSIS =====")
    print(f"\nTotal Job Listings: {len(df)}")

    print("\n===== JOB DETAILS =====")
    print(df.to_string(index=False))

    # Analyze required skills
    all_skills = []

    for skills_text in df["Skills"]:
        skills = [
            skill.strip()
            for skill in skills_text.split(",")
            if skill.strip()
        ]
        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    skills_df = pd.DataFrame(
        skill_counts.most_common(),
        columns=["Skill", "Count"]
    )

    skills_df.to_csv(SKILLS_FILE, index=False)

    print("\n===== TOP REQUIRED SKILLS =====")
    print(skills_df.to_string(index=False))

    print("\n===== MOST COMMON JOB ROLES =====")
    print(df["Job Title"].value_counts().to_string())

    print("\n===== JOB LOCATIONS =====")
    print(df["Location"].value_counts().to_string())

    print("\nAnalysis completed successfully!")
    print(f"Saved: {OUTPUT_FILE.name}")
    print(f"Saved: {SKILLS_FILE.name}")


def main():
    print("===== JOB LISTINGS SCRAPER =====")
    print("Source: Local practice HTML dataset")

    jobs = extract_jobs()
    analyze_jobs(jobs)


if __name__ == "__main__":
    main()
