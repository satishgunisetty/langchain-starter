from dotenv import load_dotenv
import requests
import os

load_dotenv()

GIST_FILE = "https://gist.githubusercontent.com/satishgunisetty/34db6e6c88333bf44943fc65d749bc13/raw/f069b3c6376eb565a055ad67db467f6e9f8154b8/manju_linkedin_scrapin.json"
SCRAPIN_API_ENDPOINT = "https://api.scrapin.io/enrichment/profile"


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """Scrapes the LinkedIn profile page of a person.
    We are mocking as well this method to get the information from a gist file
    which contains LinkedIn information.
    """
    linkedin_profile_url = linkedin_profile_url

    if mock:
        linkedin_profile_url = GIST_FILE
        response = requests.get(
            url=linkedin_profile_url,
            timeout=20,
        )
    else:
        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }

        response = requests.get(
            url=SCRAPIN_API_ENDPOINT,
            params=params,
            timeout=20,
        )

    return response.json().get("person")
