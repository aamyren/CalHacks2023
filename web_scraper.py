import praw
import pandas as pd
import datetime as dt
import sys
import json
from time import strftime, localtime
from tqdm import tqdm


class WebScraper:
    def __init__(self):
        pass

    def scraper(self, search_term, keyword, limit, scrape_comments):
        # set up your Reddit account and client info here
        reddit = praw.Reddit(
            client_id="",  # your reddit client id here
            client_secret="",  # your client secret token here
            user_agent="practice sentiment analysis",
            username="", # your reddit username here
            password="", # your reddit password here
        )

        if len(sys.argv) > 1:
            search_term = sys.argv[1]

        if len(sys.argv) > 2:
            keyword = sys.argv[2]

        print("--- Begin scraping ---")
        print("Subreddit: ", search_term)
        print("Keyword: ", keyword)

        subreddit = reddit.subreddit(search_term)

        resp = subreddit.search(keyword, int(limit))

        data_list = []

        for submission in tqdm(resp, total=limit):
            # get each submission info from resp
            data = {}
            data["ID"] = submission.id
            # print ("=ID: ",submission.id)
            data["Time"] = str(dt.datetime.fromtimestamp(submission.created))
            data["Title"] = str(submission.title.encode("ascii", "ignore"))
            data["Score"] = str(submission.score)
            data["URL"] = str(submission.url.encode("ascii", "ignore"))
            data["Text"] = str(submission.selftext[:1000].encode("ascii", "ignore"))
            # scrape comments
            comments = []
            if scrape_comments is True:
                # get top level comments for posts, with timestamps
                for top_level_comment in submission.comments:
                    comment_data = {"top_level": [], "timestamp": []}
                    if hasattr(top_level_comment, "body"):
                        comment_data["top_level"].append(str(top_level_comment.body))
                        utc = strftime(
                            "%Y-%m-%d %H:%M:%S",
                            localtime(top_level_comment.created_utc),
                        )
                        comment_data["timestamp"].append(utc)
                        comments.append(comment_data)

            # combine comment data into data_list
            data["comments"] = comments
            data_list.append(data)

            # pprint.pprint(data_list)

            pd.DataFrame(data_list)

        # write scraped data into jsons
        json_obj = json.dumps(data_list, indent=1)
        with open(
            "scraped_data/data-reddit_" + search_term + "-" + keyword + ".json", "w"
        ) as f:
            f.write(json_obj)

        print("--- Scraping done! ---")
        return None
