#########################################
## STEP 1: Import required libraries   ##
#########################################

from progressive_py.spinner import Spinner, hide_cursor, show_cursor
spinner = Spinner()
spinner.start()
spinner.final_text = '<=== Wikipedia Info Retriever ===>'
spinner.text = "Initializing: Loading Libraries..."

from langchain_openai import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

###############################
## STEP 2: Load environment  ##
###############################

spinner.text = "Initializing: Loading env Variables..."
load_dotenv()

################################
## STEP 3: Initialize the LLM ##
################################

spinner.text = "Initializing: Initializing llm..."
llm = ChatOpenAI(
    temperature=0.3,  # lower = more factual
    model="glm-4.7-flash",
    openai_api_base="https://api.z.ai/api/paas/v4/"
)

##########################################
## STEP 4: Setup Wikipedia Retriever    ##
##########################################

spinner.text = "Initializing: Creating wiki tool instances..."
wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=5000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki)

####################################
## STEP 5: Create Prompt Template ##
####################################

spinner.text = "Initializing: Crafting prompt template..."
prompt = PromptTemplate(
    input_variables=["topic", "wiki_data"],
    template="""
You are a Wikipedia-based AI Information Retriever.

Topic:
{topic}

Wikipedia Data:
{wiki_data}

Your task:
- Explain the topic clearly using the Wikipedia data
- Do NOT add fake information
- Keep it informative and structured
- Language of response should be {language}

Format:

Explanation:
...

Key Points:
- ...
- ...
"""
)

##########################
## STEP 6: Create Chain ##
##########################

spinner.text = "Initializing: Defining chain..."
chain = prompt | llm

spinner.stop()

################################
## STEP 7: CLI Interface      ##
################################

if __name__ == "__main__":
    while True:
        topic = input("Enter topic (or type 'exit'): ")
        language = input("Language (ur/en/zh): ")
        language = language.lower().strip() or 'en'
        if language not in ['ur', 'en', 'zh']:
            print("Language can only be en (english), urdu (ur) or chinese (zh).")
            continue
        if topic.lower() == "exit":
            print("Exiting...")
            break
        hide_cursor()
        spn = Spinner()
        spn.show(); spn.start()
        spn.text = "Retrieving data..."
        wiki_data = wiki_tool.run(topic)
        spn.text = "Generating Response..."
        response = chain.invoke({
                "topic": topic,
                "wiki_data": wiki_data,
                "language": {"ur": "Urdu", "en": "English", "zh": "Chinese Simplified"}[language]
            })
        show_cursor()
        spn.final_text = response.content
        spn.stop(); spn.hide()
        print('-'*60)
