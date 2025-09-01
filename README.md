# GitHub Top Repo CLI

This is a Python command-line tool to fetch the **most starred GitHub repositories** created within a specified date range.  
This tool is designed to help developers, researchers, and enthusiasts to quickly explore trending projects, discover innovative repositories, and keep track of popular projects in the GitHub ecosystem.  

By providing a simple interface to query repositories by creation date and sort them by popularity, users can gain insights into emerging trends, popular programming languages, and open-source activity over time.

---

## Motivation

With thousands of repositories being created on GitHub every day, it can be challenging to keep up with the most impactful projects.  
This tool was created to bridge that gap, giving developers a quick way to see which projects are gaining traction.

The tool is designed to be **easy to use**, **fast**, and **reliable**. 

---

## Features

- Fetch the **top 5 starred repositories** by default for the last 7 days.
- Allow users to specify a **custom date range** for repository search.
- Display repository **name**, **star count**, and **URL** for easy access.
- Lightweight, works on any machine with Python installed.

---

## Install dependencies:

pip install requests

## Usage:
- Default (7 days): python star.py
- Custom date range: python star.py --start YYYY-MM-DD --end YYYY-MM-DD



