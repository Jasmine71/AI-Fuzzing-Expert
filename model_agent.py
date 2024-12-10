import pprint
import urllib.parse
import json5
import os
from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool

#configure the LLM for the agent.
llm_cfg = {
    #'model': 'Qwen/Qwen2.5-1.5B-Instruct', # not fine-tuned remote model
    'model': 'Qwen2.5-1.5B-Instruct-lora', # local fine-tuned model
    'model_server': 'http://localhost:8000/v1',  #base URL of the model server
    'api_key': 'EMPTY',  #if no authentication is required, leave as 'EMPTY'.

    #LLM hyperparameters for generation:
    'generate_cfg': {
        'top_p': 0.8,
        'temperature': 0.7,
        'max_tokens': 2048
    }
}

#define the system behavior for the fuzzing expert.
system_instruction = '''You are a fuzzing expert assistant.
Your responsibilities include:
1. Analyzing the source code provided by the user to identify potential attack surfaces.
2. Generating seed inputs based on the source code analysis.
3. Guiding the user through setting up and executing a fuzzing process.
4. Offering advice on how to interpret and address fuzzing results, such as crashes or hangs.
When generating outputs, explain your reasoning clearly and provide actionable steps.'''

#create the fuzzing agent.
bot = Assistant(
    llm=llm_cfg,
    system_message=system_instruction
)

#define a function to handle queries via the bot.
def handle_query(fuzzer_selection, source_code, problem_description, messages):
    query = f"Fuzzer: {fuzzer_selection}\nSource Code: {source_code}\nProblem Description: {problem_description}"
    # Append the user query to the chat history.
    messages.append({'role': 'user', 'content': query})
    # Stream the bot responses token by token.
    for response in bot.run(messages=messages):
        yield response[0]['content']  # Yield each token or part of the response as it's generated.

    # response = []
    # for response in bot.run(messages=messages):
    #     # Streaming output.
    #     # print('bot response:')
    #     # pprint.pprint(response, indent=2)
    #     continue
    # # Append the bot responses to the chat history.
    # messages.extend(response)
    # return response[0]['content']

#for local inference only
if __name__ == "__main__":
    messages = []  # Stores the chat history.
    while True:
        query = input('user query: ')
        # Append the user query to the chat history.
        messages.append({'role': 'user', 'content': query})
        response = []
        for response in bot.run(messages=messages):
            # Streaming output.
            # print('bot response:')
            # pprint.pprint(response, indent=2)
            continue
        # Append the bot responses to the chat history.
        messages.extend(response)
        print(response[0]['content'])
