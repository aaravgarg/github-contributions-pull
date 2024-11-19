import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_github_contributions(username_or_url):
    """
    Fetches the number of contributions in the last year from a GitHub profile.
    :param username_or_url: GitHub username or profile URL
    :return: Number of contributions or an error message
    """
    # Initialize Selenium WebDriver (this will open a Chrome browser window in the background)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ensure headless mode is set for background running
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (if any)
    options.add_argument("--no-sandbox")  # No sandboxing, another option to improve headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Check if input is a URL or just a username
    if username_or_url.startswith("http"):
        url = username_or_url
    else:
        url = f"https://github.com/{username_or_url}"

    try:
        # Open the GitHub profile URL
        driver.get(url)

        # Simulate loading delay with a cleaner progress indicator
        print("Loading page, please wait...")
        for i in range(30):
            sys.stdout.write(f"\rLoading: {i + 1}/30")
            sys.stdout.flush()
            time.sleep(0.1)  # Simulate loading time (adjust if necessary)

        print("\n")  # Move to the next line after the progress bar

        # Find the contributions element
        contributions_element = driver.find_element(By.XPATH, '//h2[contains(text(), "contributions")]')

        # Return the text of contributions if found
        return contributions_element.text.strip()
    except Exception as e:
        return f"Error: {e}"
    finally:
        driver.quit()  # Close the browser

if __name__ == "__main__":
    profile_input = input("Enter GitHub profile URL or username: ").strip()
    contributions = get_github_contributions(profile_input)
    print(f"Result: {contributions}")
