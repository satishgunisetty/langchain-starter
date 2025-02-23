SUMMARY_PROMPT = """
    Given the information {information} about a person, With that information i want you to create:
    1. A short summary
    2. Two interesting facts about them.
"""

LINKEDIN_PROMPT = """
    Given the LinkedIn information {information} about a person, With that information i want you to create:
    1. A short summary
    2. Two interesting facts about them.
    \n{format_instructions}
"""

LINKEDIN_LOOKUP_PROMPT = """
    Given the full name {person_name}, I want you to get me a link of their LinkedIn profile page.
    Your answer should contain only a URL.
"""
