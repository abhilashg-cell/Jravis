import webbrowser
from Brain.personality import jarvis_speak

def open_website(url: str):
    """
    Opens a specific URL in the default browser.
    """
    if "http" not in url:
        url = "https://" + url
        
    jarvis_speak(f"Opening {url}...", mood="neutral")
    webbrowser.open(url)

def search_google(query: str):
    """
    Performs a Google search using the browser.
    """
    jarvis_speak(f"Searching Google for {query}...", mood="neutral")
    query = query.replace(" ", "+")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_bing(query: str):
    """
    Performs a Bing search using the browser.
    """
    jarvis_speak(f"Searching Bing for {query}...", mood="neutral")
    query = query.replace(" ", "+")
    webbrowser.open(f"https://www.bing.com/search?q={query}")
