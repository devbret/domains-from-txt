# Domains From TXT

Extracts, cleans and deduplicates all domains from URLs in a `.TXT` file and outputs them as a sorted list.

## Overview

Reads a text file containing unstructured content, identifies and extracts all URLs, cleans them to remove any trailing punctuation artifacts and then uses the `tldextract` library to parse each URL into its components to isolate the registrable domain. This application collects these domains into a set in order to ensure uniqueness, sorts them alphabetically for consistency and writes the final list as a stacked output to a new text file. Thereby producing a clean, deduplicated inventory of all distinct domains referenced within the original input.

## Set Up Instructions

Below are the required software programs and instructions for installing and using this application.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps For Use

1. Install the above programs

2. Open a terminal

3. Clone this repository using `git` by running the following command: `git clone git@github.com:devbret/domains-from-txt.git`

4. Navigate to the repo's directory by running: `cd domains-from-txt`

5. Create a virtual environment with this command: `python3 -m venv venv`

6. Activate your virtual environment using: `source venv/bin/activate`

7. Install the needed dependencies for running the script: `pip install -r requirements.txt`

8. Add your source `.TXT` file to the root of this repo

9. Rename your newly added `.TXT` file to `input.txt`

10. Run the program using this command: `python3 app.py`

11. Any domains detected from within your `input.txt` file will be output at the root as another `.TXT` file

12. To exit the virtual environment, type this command in the terminal: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Scan a text file to identify and extract all valid domain names using regex and the `tldextract` library

- Remove duplicate domains, sort uniques and write them line-by-line to an output `.TXT` file

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
