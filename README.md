<!-- ABOUT THE PROJECT -->

# About The Project

![Scraper tag][product-screenshot]

This python script do:

- scrape price of Amazon's products by URL
- outputs price directly to the console

This is a console program that extracts a price of a Amazon product given URL as argument.

## Built With

- [Python](https://www.python.org)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

## Prerequisites

This application requires the following software components:

- Python (I recommend install as a virtual environment).

  To install Python follow instructions at https://www.python.org. After Python installation on your system run these commands in the project folder :

  ```sh
  pip install virtualenv
  virtualenv venv
  ./venv/Scripts/activate
  ```

  Install these Python librarys on your system or virtual environment:

- Beautiful Soup

  ```sh
  pip install bs4

  ```

## Installation

- See the prerequisites above and clone the repo inside a folder.

```sh
git clone https://github.com/vol-automation/webscraping-amazon_product_price_scraper.git
```

## Usage

Copy an Amazon product's URL and in the console run:

- Windows:

  ```sh
  get_price_amazon "url-that-you-copied"
  ```

  practical example:

  ```sh
  get_price_amazon "https://www.amazon.com/Automate-Boring-Stuff-Python-Programmimg/dp/1593275994/"
  ```

  - IMPORTANT: preferably paste URL between double quotes

- Any system:

  ```sh
  py main.py "url-that-you-copied"
  ```

  practical example:

  ```sh
  py main.py "https://www.amazon.com/Automate-Boring-Stuff-Python-Programmimg/dp/1593275994/"
  ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: images/tag.png
