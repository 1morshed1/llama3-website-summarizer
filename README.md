# llama3-website-summarizer
Summarize any webpage using a local Large Language Model (LLM) like llama3.2 via Ollama. This tool fetches and cleans webpage content, then uses a chat-style LLM to generate a clean summary in markdown format.

✨ Features

    🧠 Uses local LLMs like llama3 (via Ollama)

    🌐 Parses and cleans webpage text using BeautifulSoup

    📝 Generates short, readable markdown summaries

    ✅ Skips scripts, ads, navigation, etc.

    📦 Lightweight, no external OpenAI dependency


🚀 Demo

    $ python summarizer.py
    Enter a URL: https://cnn.com

    ##Summary of CNN Website

    The CNN website is a news and media outlet that provides breaking news, in-depth analysis, and feature articles on a wide range of topics, including:


⚙️ Requirements

    pip install -r requirements.txt

You also need a local model via Ollama:

    ollama run llama3

Make sure Ollama is running at: http://localhost:11434


🧪 Usage

        from summarizer import display_summary

        display_summary("https://example.com")

    Or directly from the command line:

        python summarizer.py

🧠 How It Works

    Website class downloads and strips irrelevant HTML elements

    Prompt is crafted with the cleaned content

    Sends a system and user prompt to your local LLM (llama3.2)

    Markdown summary is displayed in terminal or Jupyter

🛠 Configuration

    To change the system behavior, edit this line in summarizer.py:

        system_prompt = "You are an assistant that analyzes websites and summarizes them. Respond in markdown."


📌 Future Ideas

    Batch summarize from a list of URLs

    Export summaries to .md or .pdf

    GUI or Streamlit interface

    Categorize or tag page content automatically


