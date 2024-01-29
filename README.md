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
python3 gitprobe.py -r -c "python"
```
