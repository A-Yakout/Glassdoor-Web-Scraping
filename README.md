# Glassdoor-Web-Scraping
# 🕷️ Glassdoor Job Scraper - Data Analyst Positions (Egypt)

This project scrapes job listings for **Data Analyst** roles from [Glassdoor](https://www.glassdoor.com/), specifically targeting the **Egypt** region.  
It uses **Selenium** to simulate human interaction with the dynamic site and extract structured job data for analysis or visualization.

---

## 🚀 Features

- Scrapes dynamically loaded content using **Selenium WebDriver**
- Automatically scrolls the page and clicks **"Show More Jobs"** until all jobs are loaded
- Extracts:
  - Job title
  - Company name
  - Location
  - Posting time
  - Job description
  - Job link
- Filters duplicate listings using job IDs
- Saves results to an **Excel (.xlsx)** file

---

## 🧠 Why This Project is Interesting

- Glassdoor uses dynamic content loading, which means **standard scraping with BeautifulSoup doesn't work.**
- One of the biggest challenges was handling the **"Show More Jobs"** button:
  - It appears only after scrolling
  - It may disappear/reload based on how many jobs are shown
- Selenium was used to:
  - Scroll until the button appears
  - Click it repeatedly to load more results
  - Extract structured content from dynamically updated HTML

---

## 👤 Author

Eng. Abdelrahman Yakout

📌 Data Analyst | Python Developer | Web Scraping Enthusiast

