import json

import os


class DataGenerator:
    def __init__(self):
        pass

    # generate formatted data
    def generate_data(self, filename):
        # make processed data directory
        if not os.path.exists("processed_data"):
            os.makedirs("processed_data")

        # write processed data (in this case, data and timestamps)
        json_obj = json.dumps(
            self.process_timestamps(self.load_data(filename)), indent=22
        )
        with open("processed_data/" + filename.split("/")[1], "w") as f:
            f.write(json_obj)

    # loads the data from files
    def load_data(self, filename):
        f = open(filename, "r")
        json_obj = json.load(f)

        return json_obj

    # process timestamps and comments, formatting
    # these methods can be customized in the future
    def process_timestamps(self, json_obj):
        item_list = []
        for item in json_obj:
            # format time, text, comment, and timestamp info
            item_list.append([item["Time"], item["Text"]])
            for comment_item in item["comments"]:
                item_list.append([comment_item["timestamp"], comment_item["top_level"]])

        return item_list
