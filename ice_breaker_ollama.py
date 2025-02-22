from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.prompts import SUMMARY_PROMPT

information = """
Sachin Ramesh Tendulkar born 24 April 1973) is an Indian former international cricketer who captained the Indian national team. He is widely regarded as one of the greatest cricketers of all time,[5] and is the holder of several world records, including being the all-time highest run-scorer in both ODI and Test cricket,[6] receiving the most player of the match awards in international cricket,[7] and being the only batsman to score 100 international centuries.[8] Tendulkar was a Member of Parliament, Rajya Sabha by presidential nomination from 2012 to 2018.[9][10]

Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for over 24 years.[11] In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[12] The same year, Tendulkar was a part of the team that was one of the joint-winners of the 2002 ICC Champions Trophy. Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[13] He had previously been named "Player of the Tournament" at the 2003 World Cup.
"""

if __name__ == "__main__":

    load_dotenv()

    prompt_template = PromptTemplate.from_template(
        template=SUMMARY_PROMPT
    )


    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )


    chain = prompt_template | llm | StrOutputParser()

    result = chain.invoke(input={"information": information})

    print(result)