# Job Listings Scraper

A lightweight Python web scraper that extracts job postings from the Real Python Fake Jobs portal and exports them to CSV.

## Technologies
- **Python 3**
- **Requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing
- **CSV** — structured data export

## Setup & Usage

```bash
# Clone the repository
git clone [https://github.com/yask214/job-listing-scrapper.git](https://github.com/yask214/job-listing-scrapper.git)
cd job-listing-scrapper

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # or source venv/bin/activate.fish

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scraper.py
