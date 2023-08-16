## CalHacks2023 - Exploration of sentiment analysis with GPT-4
Project for the CalHacks 2023 AI hackathon at UC Berkeley, exploring sentiment analysis with the new GPT-4 API. It involves a web scraper to collect public forum stock discussions in to data that can be processed and used to train a language model, and an chatbot interface for users to interact directly with this model. Since this is an experimental project in which the majority of this code was completed in the 36-hour span of the hackathon, it had to be cleaned up a bit before being made in a public repo, and will hopefully be improved and further expanded in the future (.❛ ᴗ ❛.)


You can check out the details & potential future improvements for this project here:

https://devpost.com/software/reddit-stock-discussion-chatbot

### Overview
Sample scraped data and sample processed documents are available in the  `sample-data` and  `sample-docs` directories. The chatbot app currently runs on the data available in the demo-data directory, but the scripts for scraping and generating your own data are readily available to use in this repository. 

The easiest way for this is to directly run the `runner.py` and simply follow the prompts! You can choose to run a new scrape for any subreddits and search keywords of your choosing, which will be generated in the `scraped_data` directory. Then, you will be prompted to choose if you would like to process the scraped data before document generation. Currently, this project only supports processing in terms of reformatting every forum entry with its unique timestamp for now, but custom processing methods can be added to `data-generator` easily. The processed data is available under `processed-data`, otherwise, the documents for training will be generated directy from the scraped data. Afterwards, the runner will prompt you to launch the app for the chatbot. 

### Important Information
To run the `web_scraper.py`, you will need to add your reddit client id and information under `client_id` in the `scraper()` method to your own copy of this code. You can create your own app for this at: https://www.reddit.com/prefs/apps. 
To launch the chatbot app, you will also need an OpenAI API key, which can be obtained here: https://beta.openai.com/account/api-keys. Before launching the app, run this line in the terminal to set your API key:
`export OPENAI_API_KEY="YOUR_API_KEY_HERE"` 

Currently, the app is reading from the sample data scraped during the hackathon, available in the `demo-data` directory. To update the chatbot for custom data, just change "demo-data" in the `index = construct_index("demo-data")` in `app.py` to your `generated-docs` directory (or the name of your custom directory). The chatbot prompt as well as the app interface can all also be easily customized in the `chatbot()` function.





