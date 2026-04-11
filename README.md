# Domains From TXT

Extracts, cleans and deduplicates all domains from URLs in a `.TXT` file and outputs them as a sorted list.

## Overview

Reads a text file containing unstructured content, identifies and extracts all URLs, cleans them to remove any trailing punctuation artifacts and then uses the `tldextract` library to parse each URL into its components to isolate the registrable domain. This application collects these domains into a set in order to ensure uniqueness, sorts them alphabetically for consistency and writes the final list as a stacked output to a new text file. Thereby producing a clean, deduplicated inventory of all distinct domains referenced within the original input.
