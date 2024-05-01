import json

import requests


def get_jisho_entry(word):
    """
    Fetches dictionary entry for a given word from Jisho.org API.

    Args:
    word (str): The word to search for.

    Returns:
    dict: A dictionary containing the word's reading, meanings, and other relevant information.
    """
    # Encode the word for URL
    encoded_word = requests.utils.quote(word)
    # Jisho API endpoint
    url = f'https://jisho.org/api/v1/search/words?keyword={encoded_word}'
    # Send GET request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the relevant data if the word is found
        if data['data']:
            first_entry = data['data'][0]  # Return the first entry which is typically the most relevant
        else:
            return "No results found."
    else:
        return "Failed to retrieve data from Jisho.org"
    print(json.dumps(first_entry, indent=4))
    return data


#search = 'sword (esp. a large, double-edged one)'
