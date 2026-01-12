#  SQL Injection Vulnerability Scanner & Logger
A Defensive security tool developed in Python to automate the detection of SQL Injection vulnerabilities. The application performs Dynamic Application Security Testing (DAST)
## Features
- **Automated Testing:** Iterates through a custom list of SQL payloads.
- **SQL Database Integration:** Utilizes a SQLite backend to persist scan results, providing a historical audit log of detected vulnerabilities.
- **Error Handling:** Implemented robust try-except blocks to manage network timeouts and connection issues. 
- **Modular Design:** Uses external payload files for easy updates.

## Tech Stack
- **Language:** Python 
- **Database:** SQL (SQLite3)
- **Libraries:** Requests (HTTP/Web interaction)

## How It Works
1. **Initialize:** The script establishes a connection to 'scan_results.db' and ensures the results table schema is prepared.
2. **Payload Injection:** It reads from 'payloads.txt' and appends various SQL 'poison' characters to target URL.
3. **Detection:** The tool analyzes the HTML response. If known database error strings are found, the URL is flagged.
4. **Logging:** Findings are automatically saved to the SQL database using parameterized queries to ensure data integrity.