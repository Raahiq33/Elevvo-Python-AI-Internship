
# Job Listings Scraper & Market Analysis

## Elevvo Python Programming & AI Internship – Task 6

A Python project that extracts job listing information from an HTML practice dataset and analyzes job market patterns using BeautifulSoup and pandas.

## Features

- Extracts job titles, companies, locations, skills, and posted dates
- Cleans and processes extracted job data
- Analyzes frequently mentioned technical skills
- Analyzes job roles and locations
- Exports results to CSV files

## Technologies

- Python
- BeautifulSoup
- pandas
- HTML
- VS Code

## How to Run

Install dependencies:

    py -m pip install beautifulsoup4 pandas requests

Run the project:

    py job_scraper.py

## Local Testing Results

- Total sample listings: 6
- Python mentions: 5
- SQL mentions: 5
- Remote listings: 3
- Colombo listings: 2
- Kandy listings: 1

## Generated Files

- job_listings.csv
- top_skills.csv

## Data Source

The current version uses a locally created HTML practice dataset with fictional job listings.

The official Elevvo practice website scraping and robots.txt verification are pending until the practice page URL is available.

## Internship

Elevvo – Python Programming & AI Internship

Task 6: Job Listings Scraper & Market Analysis

## Public Website Scraping

Practice Website:
https://realpython.github.io/fake-jobs/

Script: real_jobs_scraper.py

### Features
- Scrapes 100 fictional job listings
- Extracts job titles, companies, locations, and posted dates
- Analyzes job roles and locations using pandas
- Exports scraped data to real_jobs.csv
- Handles HTTP request errors

### Ethical Scraping
Checked https://realpython.github.io/robots.txt
The URL returned HTTP 404 (not found).
This does not imply general scraping permission.
The Fake Jobs page is intended for web scraping practice.

### Data Limitations
The public practice website contains fictional jobs and
does not provide structured required-skills data.

Skill frequency analysis uses a separate, locally created
sample HTML dataset. The two datasets are not combined.
