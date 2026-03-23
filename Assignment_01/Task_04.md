# Task 4: Craft an AI agent IDEA
# What I chose? HTML GAME DEVELOPMENT AGENT

The agent will be utilized in html game development. User will provide prompt and will get results. How it works:

### FlowChart:

![FlowChart](Task_04_AI-Agent-Workflow.svg)

### First of all, get the initial concept

We will ask user to give:

- Prompt
- Name

Then we will feed the prompt to a special AI model specifically designed to classify game prompts into specific game category. Like Arcade, Stickman or Ragdoll etc. This will make the results more better as closer to user expectation.

### Then, using the above data, develop initial prompt

We will feed Prompt, Name and predicted Type of game to the Prompt template. Prompt will require the llm to response in valid json of form:

```json
{"file_path_01": "content", "file_path_02": "content2", ...}
```

So we can just take the json and work on it. So maybe, our prompt template will look like:

```python
'''
Create an html Game named {name} of type {type}. Response should be a valid json response with keys representing the path or name of the file and values be the content of each file. For example:
{"file_path_01": "content", "file_path_02": "content2", ...}

RESPOND ONLY IN VALID JSON, NO ADDITIONAL TEXT.
'''
```

### Third: Feed to the model and parse

The llm will create the json string, and parser will convet it to python's dict form

### Executor
Executor will create the files and write their content from the generator Python's dictionary.

### The editing loop

It is obvious that user will ask agent to edit any file or add a new feature to the game. To edit the files using agent, we will first build a correct edit prompt template that will made up of:

- Context files: The files user will select to edit
- Edit Prompt: User's prompt
- Summaries of other files

We will use a summarizer that will summarize other coding files so that main llm can work smoothly with manageable context length. For example, a coding file snake.html can contain the logics and html about snake in a snake game, so, summarizer will summarize like this: "The file contains logic about snake of the game with snake image and snake styling". But the summarizer will respond like this:
```
{"file": "summary", "filepath": "summary", ...}
```
But the response will be passed directly to the prompt template.

Then, the prompt template containing:
"""
Prompt: {edit_prompt}
Edit these files {context_files_names} as:
```
{"context_file_1": "content", "context_file_2": "content"}
```
Summaries of other files:
{summary}
"""

Then we will feed this same prompt to llm and changes will be made.



