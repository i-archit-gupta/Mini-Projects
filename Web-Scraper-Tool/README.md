# Web Scraper using Python

This Python script utilizes the BeautifulSoup library to perform web scraping on a Wikipedia page that compares programming languages. The script extracts data from an HTML table, saves it as a CSV file (`language.csv`), and then converts it into an Excel file (`language.xlsx`). Below is a brief overview of the libraries used:

## Libraries Used

### 1. BeautifulSoup

- **Purpose:** BeautifulSoup is a Python library for pulling data out of HTML and XML files. It provides a convenient way to navigate, search, and modify the parse tree.
- **Installation:** You can install it using the following command:
  ```bash
  pip install beautifulsoup4
  ```

### 2. urllib

- **Purpose:** The `urlopen` function from the `urllib.request` module is used to open URLs and fetch the HTML content of a web page.
- **Installation:** It is part of the Python standard library, so no additional installation is required.

### 3. csv

- **Purpose:** The `csv` module is used for reading from and writing to CSV files. It simplifies the process of handling CSV data.
- **Installation:** It is part of the Python standard library, so no additional installation is required.

### 4. openpyxl

- **Purpose:** Openpyxl is a Python library for reading and writing Excel (xlsx) files. It allows for easy manipulation of Excel data.
- **Installation:** You can install it using the following command:
  ```bash
  pip install openpyxl
  ```

### 5. pandas

- **Purpose:** Pandas is a powerful data manipulation and analysis library. In this script, it is used to read data from the CSV file and save it as an Excel file.
- **Installation:** You can install it using the following command:
  ```bash
  pip install pandas
  ```

## Usage

1. Ensure that the required libraries are installed using the provided installation commands.

2. Run the script:
   ```bash
   python scraper.py
   ```

3. Check the generated files: `language.csv` and `language.xlsx` in the project directory.

## Customization
### 1. Change URL:

- Modify the URL in the urlopen function to scrape data from a different webpage.
### 2. Enhance Data Processing:

- Customize the script to process the extracted data further based on your requirements.

## Contribution Guidelines

Feel free to customize the script for your specific needs or contribute improvements. Follow the contribution guidelines in the repository if you have additional features or enhancements.

Happy scraping! 🌐🕸️
