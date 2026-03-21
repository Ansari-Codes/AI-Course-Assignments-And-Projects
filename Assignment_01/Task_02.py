'''
This Python file is for Task 02, stated as:

- Create a basic LangChain application that takes a user question.
- Send the question to an LLM using a prompt template.
- Return and display a clean formatted answer in the terminal.
'''

#########################################
## STEP 1: Import required library (s) ##
#########################################

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

###############################
## STEP 2: Load the env file ##
###############################

load_dotenv()

################################
## STEP 3: Initialize the LLM ##
################################

llm = ChatOpenAI(
    temperature=0.7,
    model="glm-4.7-flash",
)

####################################
## STEP 4: Create Prompt Template ##
####################################

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful AI assistant. Answer the following question clearly and concisely.

Question:
{question}

Answer:
"""
)

##########################
## STEP 5: Create Chain ##
##########################

chain = prompt | llm

################################
## STEP 6: Final QA interface ##
################################

if __name__ == "__main__":
    print("\n<=== Simple LangChain ChatApp ===>\n")
    while True:
        print("-" * 40)
        question = input("Ask (type 'exit' to quite): ")
        if question.lower() == "exit": break
        response = chain.invoke({"question": question})
        print()
        print("Bot:")
        print(response.content)
