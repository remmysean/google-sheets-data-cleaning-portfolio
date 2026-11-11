# Customer Support Ticket Data Cleaning — Google Sheets

A portfolio project demonstrating data cleaning, standardization, and analysis
in Google Sheets on a messy customer-support dataset.

Google Sheets link:  https://docs.google.com/spreadsheets/d/1hjYM7FnU5xajkp2HPWqQQal1ccJLcaOHOR9vFaZW_w8/edit?gid=1938736372#gid=1938736372

PowerPoint Presentation link: https://docs.google.com/presentation/d/1jOUdzlkAYXxGGo2ScLLchKBvBSy6slTg/edit?usp=drivesdk&ouid=105530873158588481198&rtpof=true&sd=true

## Why this project
Built for **Data Analyst** and **Technical Support Specialist** roles:
- Shows hands-on data cleaning (the #1 daily task of analysts)
- Documents decisions like a support engineer writing internal runbooks
- Delivers a summary the way you'd hand off findings to a manager

## Dataset
- 162 raw rows (150 unique + 12 duplicates)
- 8 columns: ticket_id, created_date, customer_name, email, category, priority, channel, response_time

**Issues found:** mixed date formats, duplicate IDs, casing/whitespace problems,
malformed emails, misspelled categories, blank priority fields, mixed-unit response times.

## Process
1. Duplicated the raw tab as `Working` (never edit raw)
2. Standardized names (PROPER + TRIM)
3. Cleaned emails (LOWER + SUBSTITUTE)
4. Normalized dates (DATEVALUE + fallback)
5. Mapped 11 category variants → 4 canonical values
6. Filled 8 blanks with documented default
7. Extracted numeric response days
8. Removed 12 duplicates

See [`docs/cleaning_log.md`](docs/cleaning_log.md) for step-by-step detail.

## Results
- 100% consistent date format (YYYY-MM-DD)
- 0 duplicate ticket IDs
- 0 malformed emails
- 4 canonical categories (down from 11 variants)
- Analysis: see [`docs/analysis_summary.md`](docs/analysis_summary.md)

## Files
| Path | Contents |
|---|---|
| `data/raw_tickets.csv` | Original messy data |
| `data/cleaned_tickets.csv` | Final cleaned output |
| `docs/data_dictionary.md` | Column definitions |
| `docs/cleaning_log.md` | Every transformation, in order |
| `docs/analysis_summary.md` | Insights + recommendations |
| `images/` | Before/after screenshots |

## How to reproduce
1. Import `data/raw_tickets.csv` into Google Sheets
2. Follow `docs/cleaning_log.md` step-by-step
3. Compare your output with `data/cleaned_tickets.csv`

## Tools
Google Sheets (PROPER, TRIM, LOWER, SUBSTITUTE, DATEVALUE, REGEXEXTRACT, IFS, UNIQUE, Pivot Tables)

## Author
Remission Pasurai ·(https://www.linkedin.com/in/remission-pasurai/) · remmysean@gmail.com

Verified with Python: 150 rows, 4 categories, avg response time 31.09 hours
