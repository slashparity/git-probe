# git-probe
Python-based command-line tool designed to search across various categories on GitHub for specified keywords.
It allows users to perform comprehensive searches in repositories, code, issues, and commits, providing a thorough overview of references to specific terms within GitHub public data.

## Features
Search in multiple categories: Repositories, Code, Issues, and Commits.  
Support for multiple keywords.  
OR logic in keyword search: Returns results containing any of the specified keywords.  
Secure token input: The GitHub access token is input securely and not exposed.  
Pagination handling: Retrieves all results from GitHub's paged API responses.  
Output to console and file: Search results are both displayed and saved to a file for further analysis.  

## Prerequisites

Python 3.x installed on your system.  
`requests` library installed in your Python environment (pip install requests).  

## Usage  

```bash
git clone https://github.com/yourusername/GitProbe.git
cd GitProbe
python3 gitprobe.py -r -c "iam.gserviceaccount.com"
```

This command searches for "keywords" in repositories and code.  

-r: Search in repositories.  
-c: Search in code.  
-i: Search in issues.  
-m: Search in commits.  
If no flags are provided, the script searches in all categories by default.  

The search results are displayed in the console and saved to a file named github_search_results.txt.  
The script handles GitHub API rate limits and pagination but always monitor your rate limit status to avoid being blocked.  
Use the script responsibly and ensure compliance with GitHub's terms and conditions.  
