from web_scraper import WebScraper
from data_generator import DataGenerator
from doc_generator import DocGenerator
import os

print("Welcome to Reddit Sentiment Analysis with GPT-4")

new_scrape = input("Want to run a new data scrape? [y/n]: ")
if new_scrape == "y" or new_scrape == "Y":
    search_term = input("Please type list of subreddit names to scrape: ")
    keyword = input("Please type list of relevant keywords to scape for: ")
    limit = input("Set limit to number of posts? (default=1000): ")
    try:
        limit = int(limit)
    except:
        limit = 1000
    scrape_comments = input("Scrape comments? (default=True): ")
    try:
        scape_comments = bool(scrape_comments)
    except:
        scrape_comments = True
    # testing purposes only
    search_term = ["stocks"]
    keyword = ["tsla"]

    # generate and write data for each desired term and keyword
    webscraper = WebScraper()
    if not os.path.exists("scraped_data/"):
        os.mkdir("scraped_data/")

    # run web scraper
    for term in search_term:
        for key in keyword:
            webscraper.scraper(term, key, limit, scrape_comments)

# process data into document format for training
new_docs = input("Generate new docs? [y/n]: ")
if new_docs == "y" or new_docs == "Y":
    process_data = input("Process data before generating? (default=False): ")
    try:
        process_data = bool(process_data)
    except:
        process_data = False
    if process_data is True:
        print("--- Processing data ---")
        datagenerator = DataGenerator()
        # check whether directory already exists
        if not os.path.exists("processed_data/"):
            os.mkdir("processed_data/")
        # assign directory
        directory = "scraped_data/"
        # iterate over files
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            datagenerator.generate_data(f)
        input_dir = "processed_data/"
        print("--- Processing data done! (in processed_data/ dir)")
    else:
        input_dir = "scraped_data/"
    print("--- Generating docs ---")
    # check whether directory already exists
    if not os.path.exists("generated_docs/"):
        os.mkdir("generated_docs/")
    # run doc generator
    docgenerator = DocGenerator()
    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir, filename)
        docgenerator.write_data(f)
    print("--- Generating docs done! ---")

# train gpt-4 on documents and run app
run_app = input("Run app? [y/n]: ")
if run_app == "y" or run_app == "Y":
    print("--- Running app ---")
    f = open("app.py")
    exec(f.read())
