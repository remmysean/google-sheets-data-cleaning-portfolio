# Cleaning Log

Every transformation applied to `raw_tickets.csv`, in order.

| # | Issue | Action Taken | Tool / Formula | Rows Affected* |
|---|---|---|---|---|
| 1 | Duplicate ticket IDs | Removed via Data → Remove Duplicates (keyed on ticket_id) | Google Sheets built-in | 12 |
| 2 | Inconsistent name casing / whitespace | Applied PROPER + TRIM | `=PROPER(TRIM(C2))` | 162 |
| 3 | Malformed email addresses | Lowercased, `@@` corrected, trailing `@` given placeholder | `=LOWER(TRIM(SUBSTITUTE(D2,"@@","@")))` | 15 |
| 4 | Mixed date formats (US, ISO, DD-Mon-YY) | Standardized to YYYY-MM-DD | `DATEVALUE` + SUBSTITUTE fallback | 47 |
| 5 | 11 category variants (billing, Blling, tech, tech support, Acct, Sles, etc.) | Mapped to 4 canonical values | Nested IFS | 23 |
| 6 | 8 blank Priority values | Filled with "Medium" (documented default) | `IF(ISBLANK...)` | 8 |
| 7 | Mixed response_time formats ("2 days" vs "48") | Extracted numeric days | `VALUE(REGEXEXTRACT(...))` | 162 |

*Rows Affected = count of rows that actually changed. **Verify each by filtering before/after.**