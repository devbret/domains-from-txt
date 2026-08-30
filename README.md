# Domains From TXT

Extracts, cleans and deduplicates all domains from URLs in a `.txt` file and outputs them as a sorted list.

## Application Overview

Reads a text file containing unstructured content, identifies and extracts all URLs, cleans them to remove any trailing punctuation artifacts and then uses the `tldextract` library to parse each URL into its components to isolate the registrable domain. This application collects these domains into a set in order to ensure uniqueness, sorts them alphabetically for consistency and writes the final list as a stacked output to a new text file. Thereby producing a clean, deduplicated inventory of all distinct domains referenced within the original input.

## Basic Setup Instructions

Below are the required software programs and instructions for installing and using this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps For Use

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/domains-from-txt.git`

4. Navigate to the repo's directory: `cd domains-from-txt`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Add your source text file to the root of this repo

9. Rename your file to `input.txt`

10. Run the program: `python3 app.py`

11. When finished, exit the virtual environment: `deactivate`

## Other Considerations

Below you will find information not covered in the installation and use sections above. Including the abilities this repo is setting out to demonstrate. As well as an overview of the license this code is made available with. And a way to contact the maintainer with questions, suggestions and collaboration opportunities.

### Abilities Demonstrated

This project repo is intended to demonstrate an ability to do the following:

- Identify potential domain names within large blocks of unstructured text using regular expressions

- Clean data by stripping away punctuation and special characters from extracted strings

- Use the `tldextract` library to separate core domains from subdomains and ensure consistent formatting

- Filter out duplicate entries and sorts the final list alphabetically to create an organized output file

### License Information

This repository is distributed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense and sell copies of this software, including as part of proprietary or commercial work. The single condition is the copyright and permission notices contained in the LICENSE file must be included with any copy or substantial portion of the software that you redistribute. The software is provided "as is", without warranty of any kind, and the copyright holder is not liable for any claim or damages arising from its use.

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
