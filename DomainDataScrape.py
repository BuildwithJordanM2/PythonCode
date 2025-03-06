import requests
from bs4 import BeautifulSoup

# Function to fetch and extract text from a URL
def fetch_text_from_url(url):
    headers = {
        "User-Agent": "User-Agent": "Mozilla/5.0"}
    }
    
    # Send an HTTP GET request to the URL with custom headers
    response = requests.get(url, headers=headers)
    
    # Debugging: print the status code
    print(f"Status Code: {response.status_code}")
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all text from the HTML
        text = soup.get_text()
        
        return text
    else:
        return f"Failed to retrieve content, status code: {response.status_code}"

# Example usage:
url = "https://example.com"
text = fetch_text_from_url(url)
print(text)
