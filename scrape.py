from bs4 import BeautifulSoup
import requests
import csv

# Send a GET request to the quotes website and fetch the page content
page_to_scrape = requests.get("http://quotes.toscrape.com")

# Parse the page content using BeautifulSoup with an HTML parser
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all the quotes and authors on the page
quotes = soup.find_all("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

# Open a CSV file in write mode to save the scraped data
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

# Write the header row to the CSV file
writer.writerow(["QUOTES", "AUTHORS"])

# Loop through each quote and its corresponding author, printing and saving them
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

# Close the CSV file after writing all the data
file.close()
