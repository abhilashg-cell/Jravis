import webbrowser
import urllib.parse

def search_youtube(query: str) -> tuple[bool, str]:
    """Opens YouTube search results."""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.youtube.com/results?search_query={encoded}"
        webbrowser.open(url)
        return True, f"Searching YouTube for {query}."
    except Exception as e:
        print(f"YouTube search error: {e}")
    return False, ""

def search_google(query: str) -> tuple[bool, str]:
    """Opens Google search results."""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={encoded}"
        webbrowser.open(url)
        return True, f"Searching Google for {query}."
    except Exception as e:
        print(f"Google search error: {e}")
    return False, ""

def open_youtube() -> tuple[bool, str]:
    """Opens YouTube homepage."""
    try:
        webbrowser.open("https://www.youtube.com")
        return True, "Opening YouTube."
    except:
        pass
    return False, ""
