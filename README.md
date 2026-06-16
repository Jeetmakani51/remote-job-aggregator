# Remote Job Dashboard

A data-driven dashboard that aggregates and analyzes remote job listings from We Work Remotely using Python, BeautifulSoup, Pandas, and Streamlit.

Live Demo

🔗 Dashboard: https://remote-job-aggregator-u5bgdb7vrzi6nqmzfu5nxt.streamlit.app/

## Overview

This project scrapes remote job listings, cleans and analyzes the data, and presents insights through an interactive Streamlit dashboard.

The dashboard allows users to explore hiring trends, search for jobs, filter results, and visualize key market statistics.

## Features

* Remote job scraping using BeautifulSoup
* Structured CSV data export
* Data analysis with Pandas
* Interactive Streamlit dashboard
* Job search functionality
* Company and location filters
* Salary availability filtering
* KPI metrics and hiring insights
* Visualizations for companies, locations, and job titles

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas
* Streamlit

## Key Insights

* 238 remote job listings analyzed
* 35 jobs disclosed salary information
* 23 AI-related positions identified
* Top hiring companies include Cubos Tecnologia and AHU Technologies
* Most common locations: Remote and BR
* Most frequent roles: DevOps Engineer and Senior Product Manager

## Project Structure

```text
job_aggregator/
├── scraper.py
├── jobs.csv
├── analysis.ipynb
├── app.py
└── README.md
```

## Dashboard Capabilities

* Search jobs by keyword
* Filter by company
* Filter by location
* View salary-specific opportunities
* Explore hiring trends through charts
* Analyze job market statistics

## Future Improvements

* Direct job application links
* Multi-job-board aggregation
* Automated scheduled scraping
* Advanced skill trend analysis
* Public deployment and live updates

## Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## License

This project is intended for educational and portfolio purposes.
