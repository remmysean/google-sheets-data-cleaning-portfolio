# Data Dictionary

| Column | Description | Data Type | Example | Notes |
|---|---|---|---|---|
| ticket_id | Unique ticket identifier | Text | TKT-0001 | Format: TKT-NNNN |
| created_date | Date ticket was opened | Date (YYYY-MM-DD) | 2024-01-15 | Standardized from 3 input formats |
| customer_name | Customer full name | Text | John Doe | PROPER + TRIM applied |
| email | Customer email address | Text | john.doe@gmail.com | Lowercased, `@@` corrected |
| category | Support category | Text (enum) | Billing | Mapped to: Billing, Technical, Account, Sales |
| priority | Ticket priority | Text (enum) | High | Blank values filled with "Medium" |
| channel | Contact channel | Text (enum) | Email | Email, Phone, Chat |
| response_time_days | Days until first response | Integer | 2 | Extracted from mixed text ("2 days", "48") |