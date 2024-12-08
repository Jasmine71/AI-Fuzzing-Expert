import os
import pprint
import urllib.parse
from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool

# Step 1: Configure the LLM for the agent.
llm_cfg = {
    'model': 'Qwen/Qwen2.5-7B-Instruct',
    'model_server': 'http://localhost:8000/v1',  # Base URL of the model server
    'api_key': 'EMPTY',  # If no authentication is required, leave as 'EMPTY'.

    # (Optional) LLM hyperparameters for generation:
    'generate_cfg': {
        'top_p': 0.8,
        'temperature': 0.7,
        'max_tokens': 512
    }
}

# Step 2: Define the system behavior for the fuzzing expert.
system_instruction = '''You are a fuzzing expert assistant.
Your responsibilities include:
1. Analyzing the source code provided by the user to identify potential attack surfaces.
2. Generating seed inputs based on the source code analysis.
3. Guiding the user through setting up and executing a fuzzing process.
4. Offering advice on how to interpret and address fuzzing results, such as crashes or hangs.

When generating outputs, explain your reasoning clearly and provide actionable steps.'''

# Step 3: List available tools for the agent.
tools = ['code_interpreter']  # Built-in tool for executing Python code and other functions.

# Step 4: Provide the source code files for analysis.
files = [
    os.path.abspath('./stt_project/target/source_code/a.c'),
    os.path.abspath('./stt_project/target/source_code/b.c'),
    os.path.abspath('./stt_project/target/source_code/c.c')
] # Add paths to source code files.

# Step 5: Create the fuzzing agent.
bot = Assistant(
    llm=llm_cfg,
    system_message=system_instruction,
    function_list=tools,
    files=files
)

# Step 6: Run the agent interactively as a chatbot.
def run_fuzzing_agent():
    print("Fuzzing Expert Agent is running...")
    messages = []  # This stores the chat history.
    while True:
        # Get the user's input.
        query = input('User query: ')
        
        # Append user query to the message history.
        messages.append({'role': 'user', 'content': query})
        
        # Run the agent with the messages.
        print("Agent response:")
        for response in bot.run(messages=messages):
            # Print response in a streaming fashion.
            pprint.pprint(response, indent=2)
        
        # Append the bot's response to the message history.
        messages.extend(response)

# Run the agent if this script is executed directly.
if __name__ == "__main__":
    run_fuzzing_agent()
