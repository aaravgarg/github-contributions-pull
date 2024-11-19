# GitHub Contributions Checker

This Python script allows you to fetch the number of contributions made by a GitHub user in the past year, directly from their GitHub profile. The script utilizes **Selenium WebDriver** to scrape the necessary data, and it works headlessly (without opening a browser window) for convenience.

## Features

- Fetch the number of contributions from a given GitHub profile URL or username.
- Headless browsing with **Selenium** (no browser window opens).
- Display a simple inline progress bar during data retrieval.

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python 3.x** - Make sure you have Python installed on your machine.
2. **Chrome** - The script uses Google Chrome to fetch data, and you'll need the appropriate version installed on your system.
3. **Required Python libraries** - Install the required dependencies using `pip`.

## Installation

### Step 1: Install the required Python packages

You can install the required packages using `pip` by running the following command in your terminal:

```bash
pip install selenium webdriver-manager
