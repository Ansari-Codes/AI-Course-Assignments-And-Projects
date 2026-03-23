'''
This Python file is for Task 03, stated as:

- Build one small AI tool using Python + LangChain.
- Examples: AI Study Assistant, AI Email Generator, or AI Idea Generator.
- The tool should take user input and generate helpful output.

What m gonna do? I will build a "Wikipedia Info Retriever"
- User will enter the topic
- User will choose the language
- User will get the information on that topic retrieved from wikipedia
Feature: Interactive response with bullet points and explainations, easy to understand, tri-lingual
Note: Only chinese, english and urdu are supported yet
'''

'''
Required Tools:

- langchain and related libraries
- wikipedia tools and utilities
- progressive_py library: A library to create interactive cli visuals for loading (created by me 😏, you can get it on github: https://github.com/Ansari-Codes/progressive_py)
'''

#########################################
## STEP 1: Import required libraries   ##
#########################################

from progressive_py.spinner import Spinner, hide_cursor, show_cursor
from progressive_py.manager import AssetsManager

try:
    manager = AssetsManager()
    loading_spinner_style = manager.load("spinner", "style", "dotsCircle")
    loading_spinner_theme = manager.load("spinner", "theme", "matrix")
    llm_spinner_style = manager.load("spinner", "style", "bouncingBall")
    llm_spinner_theme = manager.load("spinner", "theme", "cyberpunk")
except Exception as e:
    print(e)
    loading_spinner_style =  ['|', '/', '-', '\\']
    loading_spinner_theme = {}
    llm_spinner_style =  ['|', '/', '-', '\\']
    llm_spinner_theme = {}

spinner = Spinner(seq=loading_spinner_style, spn_side="left", interval=0.08, **loading_spinner_theme)
spinner.start()
spinner.final_text = '<=== Wikipedia Info Retriever ===>'
spinner.text = "Loading Libraries..."

from langchain_openai import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

###############################
## STEP 2: Load environment  ##
###############################

spinner.text = "Loading env Variables..."
load_dotenv()

################################
## STEP 3: Initialize the LLM ##
################################

spinner.text = "Initializing llm object..."
llm = ChatOpenAI(
    temperature=0.3,  # lower = more factual
    model="glm-4.7-flash",
    openai_api_base="https://api.z.ai/api/paas/v4/"
)

##########################################
## STEP 4: Setup Wikipedia Retriever    ##
##########################################

spinner.text = "Initializing wiki tool instances..."
wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=5000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki)

####################################
## STEP 5: Create Prompt Template ##
####################################

spinner.text = "Crafting prompt template..."
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

Follow this Format:

Overview:
...

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

spinner.text = "Defining chain..."
chain = prompt | llm

spinner.stop()

################################
## STEP 7: CLI Interface      ##
################################

if __name__ == "__main__":
    while True:
        topic = input(">>> Enter topic (or type 'exit'): ")
        language = input(">>> Language (ur/en/zh): ")
        language = language.lower().strip() or 'en'
        if language not in ['ur', 'en', 'zh']:
            print("Language can only be en (english), urdu (ur) or chinese (zh).")
            continue
        if topic.lower() == "exit":
            print("Exiting...")
            break
        hide_cursor()
        spn = Spinner(seq=llm_spinner_style, spn_side="left", interval=0.08, **llm_spinner_theme)
        spn.show(); spn.start()
        spn.text = "Retrieving data..."
        wiki_data = wiki_tool.run(topic)
        spn.text = "Generating Response..."
        response = chain.invoke({
                "topic": topic,
                "wiki_data": wiki_data,
                "language": {"ur": "Urdu", "en": "English", "zh": "Chinese (Simplified)"}[language]
            })
        show_cursor()
        spn.final_text = ">>> Response"
        spn.stop(); spn.hide()
        print(response.content)
        print('-'*60)
