# aiNewsSummaryGenerator

## Application Description

The AI News Summary Generator gets the headlines from the technology section of the New York Times using the NYT Section API. Once retrieved, the summary generator passes the list of headlines to the Anthropic API and requests a summary of those headlines. The application then puts the text of the summary in a file title summary-{todaysDate}.txt. A new file will be generated on a daily basis. If you run the application multiple times in the same day, the summary file for that day will only contain the summary from the most recent run of the application.

Anthropic Client Parameters:

- Model: claude-3-haiku-20240307
- System Description: You are working as a blogger trying to summarize the AI news of the day.
- Messaging Role: user
- Prompt: Here are some headlines realated to AI from todays news, can you write me a one paragraph summary of what is happening today? Please do not add any extra text. Just tell me the summary.\n{headlines}

## Application External Requirements

- python3

## Run Instructions

1. Install dependencies using pip3. Dependency list is stored in requirements.txt
2. Generate API keys for both the NYT Section API and the Anthropic API. Put those in a `.env` file that follows the format of the template in `.env.template`.
3. Run application using command `python3 get_ai_news.py`
