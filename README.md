# Land.id Property Details Automation

This Python project automates the process of logging into [Land.id](https://land.id/), retrieves an authentication token from the `sign_in.json` network response, and then fetches property details based on geographic coordinates (latitude and longitude). The retrieved data is saved in a `parcel_details.json` file.

## Table of Contents
- [Project Overview](#project-overview)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)

## Project Overview

This project uses the Playwright library to:
1. **Log into Land.id**: It automates the login process using the user's credentials (email and password).
2. **Capture Authentication Token**: The script captures the `authentication_token` and `email` from the network response of `sign_in.json`.
3. **Fetch Property Details**: Using the token and email, it makes a request to the Land.id API to fetch property details based on latitude and longitude.
4. **Save Response**: The property details are saved in a `parcel_details.json` file.

## Dependencies

This project uses the following libraries:
- **[Playwright](https://playwright.dev/python/docs/intro)**: For browser automation and network interception.
- **asyncio**: For asynchronous execution of tasks.
- **json**: For saving the API response to a file.
- **getpass** (optional): To securely hide password input (not currently included in the main flow but can be used).

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/SId-pranay123/landid-automation.git
cd landid-automation
```
### Step 2: Install Python Dependencies

Ensure you have Python installed (version 3.7 or higher).
Install Playwright and its dependencies:
```bash
pip install playwright
playwright install
```

## Usage

Run the script:
```bash
python3 script.py
```

Enter the required information:

The script will prompt you for your email, password, latitude, and longitude.


### If you can't install playwright in python global, try it in virtual environment: 

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
```

make sure to change the path/to/venv with your desired path. 