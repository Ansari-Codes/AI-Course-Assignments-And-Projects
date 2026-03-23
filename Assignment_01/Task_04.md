# Task 4: Craft an AI agent IDEA
# What i chose? HTML GAME DEVELOPMENT AGENT

The agent will be utilized in html game development. User will provide prompt and will get results. How it works:

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

'''
```

### Third: Feed to the model

