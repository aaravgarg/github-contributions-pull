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

```pip install selenium webdriver-manager```

### Step 2: Download the appropriate WebDriver

The script uses Selenium WebDriver to control the Chrome browser. The WebDriver will be automatically installed for you using the webdriver-manager library, so you don’t need to manually download and configure the WebDriver.

### Step 3: Save the script

Save the script as github_contributions.py in your project folder.

## Usage

Run the script:

```python github_contributions.py```

Input: When prompted, enter a GitHub profile URL or just the username of the user whose contributions you want to check.

### Example input:

```Enter GitHub profile URL or username: aaravgarg```

Progress Bar: While the script is retrieving the contribution data, a simple inline progress bar will be shown in your terminal.

Result: The script will display the number of contributions made by the user in the past year.

Example output:

```
Loading: 30/30

Result: 120 contributions in the last year
```

License: This project is licensed under the MIT License - see the LICENSE file for details.

Created with ❤️ by Aarav Garg




