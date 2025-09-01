import argparse #Allows us to read options typed in the terminal
import requests 
#Github API
from datetime import datetime, timedelta #work with dates

BASE_URL = "https://api.github.com/search/repositories" #Github search repo API

def fetch_repos(start_date=None, end_date=None): #function that gets the repos
    if start_date and end_date: #if date is provided
        date_range = f"{start_date}..{end_date}"
    else:
        # Default: last 7 days
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')
        date_range = f"{start_date}..{end_date}"

    url = f"{BASE_URL}?q=created:{date_range}&sort=stars&order=desc&per_page=10"
    response = requests.get(url) #send request to github
    response.raise_for_status() #Throws errors if needed
    return response.json() #covert from JSON to Python dictionary

def main():#running the script
    parser = argparse.ArgumentParser(description="Get most starred GitHub repos in a date range.")
    parser.add_argument("--start", help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end", help="End date in YYYY-MM-DD format")
    args = parser.parse_args()

    data = fetch_repos(args.start, args.end)
    for repo in data["items"]:
        print(f"{repo['name']} ⭐ {repo['stargazers_count']} | {repo['html_url']}")

if __name__ == "__main__": #run when python star.py is typed 
    main()
