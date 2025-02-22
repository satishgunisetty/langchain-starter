import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_finder import lookup
from prompts.prompts import LINKEDIN_PROMPT

if __name__ == "__main__":
    load_dotenv()
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
    AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

    prompt_template = PromptTemplate.from_template(
        template=LINKEDIN_PROMPT,
    )

    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0)

    azure_llm = AzureChatOpenAI(
        azure_deployment=AZURE_DEPLOYMENT_NAME,
        api_version=AZURE_API_VERSION,
        temperature=0,
    )

    linkedin_url = lookup(name="Satish Gunisetty Epam", llm=azure_llm)

    linkedin_user_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=False
    )

    chain = prompt_template | azure_llm | StrOutputParser()

    output = chain.invoke(input={"information": linkedin_user_data})

    print(output)
