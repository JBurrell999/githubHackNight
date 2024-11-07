import requests

Wiki_API_KEY = 'your_api_key_here'
BASE_URL = 'https://enterprise.wikimedia.com/docs/on-demand/'

def get_wiki_document(title):
    """
    Fetch a Wikipedia document by title using Wikimedia Enterprise API.

    Args:
        title (str): The title of the Wikipedia article to retrieve.

    Returns:
        dict: JSON response containing the Wikipedia document details.
    """
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    params = {
        'title': title,
        'format': 'json'
    }
    
    response = requests.get(f"{BASE_URL}page", headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  
    else:
        print(f"Error: {response.status_code}")
        return None

document_title = "Python (programming language)"
wiki_document = get_wiki_document(document_title)

if wiki_document:
    print(wiki_document)
