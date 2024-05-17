import random
import wikipediaapi


def get_random_language():
    # Dictionary of Indian languages along with their language codes
    indian_languages = {
        'English': 'en',
        "Hindi": "hi",
        "Bengali": "bn",
        "Marathi": "mr",
        "Telugu": "te",
        "Tamil": "ta",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Urdu": "ur",
        "Punjabi": "pa",
        "Odia": "or",
    }

    # Randomize the keys (language codes)
    randomized_codes = list(indian_languages.values())
    random.shuffle(randomized_codes)

    # Return the randomized language codes
    return randomized_codes


def get_random_article_content():
    """Gets a random article content of a random language.

    Returns:
      A string containing the content of the random article.
    """

    wiki = wikipediaapi.Wikipedia(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        language=get_random_language()[0]
    )

    # Get a random page in the chosen language.
    page = wiki.page("india")

    # Get the content of the page.
    content = page.text

    return content


# Example usage:

print(get_random_article_content())
