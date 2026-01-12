import requests
from urllib3.util import url


def check_sql_injection(url):
    # 1. Load payloads from the file
    with open("payloads.txt", "r") as file:
        payloads = file.read().splitlines()
    # 2. Loop through each 'poison' character
    for p in payloads:
        test_url = f"{url}{p}"
        print(f"Testing: {test_url}")

        try:
            response = requests.get(test_url)

            # 3. Look for SQL error messages in the website's response
            if "sql syntax" in response.text.lower() or "mysql" in response.text.lower():
                print(f"[!] VULNERABILITY FOUND: {p}")
                return #stop if one is found
        except:
            print("Error: Could not connect to site.")

    print("Scan complete. No obvious vulnerabilities found.")

# The target (a site for testing)
target = "http://testphp.vulnweb.com/artists.php?artist="
check_sql_injection(target)