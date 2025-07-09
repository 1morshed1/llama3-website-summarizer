import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from IPython.display import Markdown, display
import sys

# Connect to Ollama's local LLM server
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Prompt given to the model
system_prompt = (
    "You are an assistant that analyzes the contents of a website and provides a short summary. "
    "Ignore navigation, buttons, and repeated elements. Respond in markdown."
)


class Website:
    def __init__(self, url):
        self.url = url
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            self.title = soup.title.string.strip() if soup.title else "No title found"
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        except Exception as e:
            self.title = "Error loading site"
            self.text = f"Failed to load the page: {e}"


def user_prompt_for(website):
    return f"""You are looking at a website titled "{website.title}".

The contents of this website is as follows. Please provide a short summary in markdown.
If it includes news or announcements, summarize those too.

{website.text}
"""


def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url):
    website = Website(url)
    try:
        response = openai.chat.completions.create(
            model="llama3.2",
            messages=messages_for(website)
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error summarizing website: {e}"


def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        url = sys.argv[1]
    else:
        url = input("Enter a website URL: ")

    summary = summarize(url)
    print("\n" + summary)
