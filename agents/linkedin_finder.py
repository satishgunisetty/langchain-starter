import os

from prompts.prompts import LINKEDIN_LOOKUP_PROMPT
from tools.tools import get_profile_url_tavily

from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from langchain import hub


def lookup(name: str, llm: AzureChatOpenAI) -> str:

    prompt_template = PromptTemplate.from_template(template=LINKEDIN_LOOKUP_PROMPT)

    tools_for_agent = [
        Tool(
            name="Crawl google for LinkedIn Profile Page",
            func=get_profile_url_tavily,
            description="Useful when you need to get the LinkedIn profile URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        handle_parsing_errors=True,
    )

    url = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(person_name=name)}
    )

    return url["output"]
