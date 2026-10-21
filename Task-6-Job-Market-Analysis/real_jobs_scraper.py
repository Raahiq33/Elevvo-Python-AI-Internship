
import requests
import pandas as pd
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT = Path(__file__).parent / "real_jobs.csv"


def scrape_jobs():
    print("===== REAL PYTHON JOB SCRAPER =====")

    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Website error: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select("div.card-content")

    jobs = []

    for card in cards:
        title = card.select_one("h2.title")
        company = card.select_one("h3.company")
        location = card.select_one("p.location")
        date = card.select_one("time")

        if not title or not company:
            continue

        jobs.append({
            "Job Title": title.get_text(strip=True),
            "Company": company.get_text(strip=True),
            "Location": (
                location.get_text(strip=True)
                if location else ""
            ),
            "Posted Date": (
                date.get("datetime", "")
                if date else ""
            )
        })

    return jobs


def analyze_jobs(jobs):
    if not jobs:
        print("No job listings found.")
        return

    df = pd.DataFrame(jobs)
    df = df.drop_duplicates()
    df = df.dropna(subset=["Job Title", "Company"])

    df.to_csv(OUTPUT, index=False)

    print(f"\nTotal Job Listings: {len(df)}")

    print("\n===== FIRST 10 JOBS =====")
    print(df.head(10).to_string(index=False))

    print("\n===== TOP JOB ROLES =====")
    print(df["Job Title"].value_counts().head(10))

    print("\n===== TOP LOCATIONS =====")
    print(df["Location"].value_counts().head(10))

    print("\nScraping and analysis completed!")
    print(f"CSV saved: {OUTPUT.name}")


if __name__ == "__main__":
    job_list = scrape_jobs()
    analyze_jobs(job_list)
