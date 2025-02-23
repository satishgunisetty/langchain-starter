import os
from typing import Tuple

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_finder import lookup
from prompts.prompts import LINKEDIN_PROMPT
from output_parser import summary_parser, Summary

AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

def process(name) -> Tuple[Summary, str]:

    prompt_template = PromptTemplate.from_template(
        template=LINKEDIN_PROMPT,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0)

    azure_llm = AzureChatOpenAI(
        azure_deployment=AZURE_DEPLOYMENT_NAME,
        api_version=AZURE_API_VERSION,
        temperature=0,
    )

    linkedin_url = lookup(name=name, llm=azure_llm)

    print(f"LinkedIn URL: {linkedin_url}")

    linkedin_user_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=True
    )

    chain = prompt_template | azure_llm | summary_parser

    output = chain.invoke(input={"information": linkedin_user_data})

    return output, linkedin_user_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()

    summary, profile_pic_url = process(name="Manjunatha K EPAM")

    print(summary)
    print(profile_pic_url)