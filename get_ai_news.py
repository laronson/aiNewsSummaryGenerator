from requests import get
from anthropic_client import AnthropicClient
from dotenv import load_dotenv
import os
from datetime import date
from textwrap import fill as tf_fill

load_dotenv(f'{os.getcwd()}/.env')


def nytTechSectionNews():
    print("Getting NYT")
    url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    res = get(url, params={"api-key": os.environ.get('NYT_API_KEY')})
    if res.status_code == 200:
        nyt_dict = res.json()
        articles = nyt_dict['results']
        titles = list(map(lambda article: article['title'], articles))
        return titles
    else:
        print("Request failed")

def writeSummaryToFile(summary:str):
    '''
    Using the with keyword helps python with context management.  It is extrememlly useful when doing things like 
    handling files or network connections.  Essentially, the with keyword tells python to do things like handle resource
    management, automatic cleanup and watch for errors (essentially wrapping the with code in a try catch).  The with
    keyword is a less verbose way of doing something like
    __enter__()
    ...code... 
    __exit__
    '''
    with open(f"{os.getcwd()}/summary-{date.today().strftime('%d-%m-%y')}.txt", 'w+', encoding='utf-8') as file:
        wrapped_text = tf_fill(summary, width=120)
        file.writelines(wrapped_text)

def run():
    client = AnthropicClient.get_instance()
    nyt_headlines = nytTechSectionNews()
    summary = client.analyze_headlines(nyt_headlines)
    writeSummaryToFile(summary)
    

if __name__ == "__main__":
    run()