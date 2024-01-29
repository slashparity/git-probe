import argparse
import requests
from getpass import getpass

# Setup command-line argument parsing
parser = argparse.ArgumentParser(description='Search GitHub for specified keywords in various categories.')
parser.add_argument('keywords', type=str, help='Keywords to search for, separated by commas (e.g., "keyword1,keyword2")')
parser.add_argument('-r', '--repositories', action='store_true', help='Search in repositories')
parser.add_argument('-c', '--code', action='store_true', help='Search in code')
parser.add_argument('-i', '--issues', action='store_true', help='Search in issues')
parser.add_argument('-m', '--commits', action='store_true', help='Search in commits')
args = parser.parse_args()

# Prompt the user to input the GitHub Personal Access Token securely
auth_token = getpass("Please enter your GitHub Personal Access Token: ")
headers = {
    'Authorization': f'token {auth_token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Parse keywords
keywords = [keyword.strip() for keyword in args.keywords.split(',')]

# Constructing the search query with OR logic
# Note: GitHub search query uses the syntax 'keyword1 OR keyword2' for OR logic
query = ' OR '.join(f'"{keyword}"' for keyword in keywords)  # Enclose each keyword in quotes

# Determine which categories to search in
categories = {
    'repositories': args.repositories,
    'code': args.code,
    'issues': args.issues,
    'commits': args.commits
}
# If no categories are specified, search all
if not any(categories.values()):
    categories = {key: True for key in categories}

# ANSI escape code for red color and reset color
RED = '\033[91m'
RESET = '\033[0m'
HORIZONTAL_LINE = RED + '-' * 80 + RESET  # 80 is the line width, adjust as needed

# Prepare the output file
output_file = 'github_search_results.txt'
with open(output_file, 'w') as file:
    for category, search in categories.items():
        if not search:
            continue
        
        url = f'https://api.github.com/search/{category}?q={query}'
        
        # Print and save category header with red horizontal lines
        category_header = f"\n{HORIZONTAL_LINE}\nSearching in {category} for keywords...\n{HORIZONTAL_LINE}\n"
        print(category_header)
        file.write(category_header + '\n')

        while url:
            response = requests.get(url, headers=headers)
            
            # Check the response
            if response.status_code == 200:
                # Parse JSON and use data
                data = response.json()
                items = data['items']
                
                for item in items:
                    result_line = f"Found in {category}: {item['html_url']}\n"
                    print(result_line)
                    file.write(result_line)
                
                # Handling pagination (check if 'next' is in the Link header)
                if 'next' in response.links.keys():
                    url = response.links['next']['url']
                else:
                    url = None
            else:
                error_message = f'Failed to retrieve {category}: {response.json()}\n'
                print(error_message)
                file.write(error_message)
                url = None

