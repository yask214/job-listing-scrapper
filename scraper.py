import csv
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs():
    """Fetches the webpage and extracts all job postings."""
    headers = {"User-Agent": "JobScraper/1.0 (Educational)"}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    results_container = soup.find("div", id="ResultsContainer")

    if not results_container:
        print("Could not find results container.")
        return []

    job_cards = results_container.find_all("div", class_="card-content")
    jobs = []

    for card in job_cards:
        title_elem = card.find("h2", class_="title")
        company_elem = card.find("h3", class_="company")
        location_elem = card.find("p", class_="location")

        title = title_elem.text.strip() if title_elem else "N/A"
        company = company_elem.text.strip() if company_elem else "N/A"
        location = location_elem.text.strip() if location_elem else "N/A"

        parent_card = card.find_parent("div", class_="card")
        link = "N/A"
        if parent_card:
            footer = parent_card.find("footer", class_="card-footer")
            if footer:
                links = footer.find_all("a")
                if len(links) >= 2 and links[1].has_attr("href"):
                    link = links[1]["href"]

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "URL": link
        })

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    """Writes a list of job dictionaries to a CSV file."""
    if not jobs:
        print("No jobs found to save.")
        return

    fieldnames = ["Title", "Company", "Location", "URL"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Done! Successfully wrote {len(jobs)} jobs to {filename}")


if __name__ == "__main__":
    print("Scraping jobs from Real Python...")
    listings = scrape_jobs()
    save_to_csv(listings)
