import os
from qwen_agent.agents import Assistant
from qwen_agent.tools.base import BaseTool, register_tool

# configure the LLM for the agent.
llm_cfg = {
    'model': 'Qwen/Qwen2.5-0.5B-Instruct',
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
]  # Add paths to source code files.

# Step 5: Create the fuzzing agent.
bot = Assistant(
    llm=llm_cfg,
    system_message=system_instruction,
    function_list=tools,
    files=files
)

# Define a function to handle queries via the bot.
def handle_query(fuzzer_selection, target_path, question_type, problem_description, custom_input):
    messages = []

    # Construct the user query based on inputs.
    if custom_input:
        query = custom_input
    else:
        query = f"Fuzzer: {fuzzer_selection}\nTarget Path: {target_path}\nQuestion Type: {question_type}\nProblem Description: {problem_description}"

    messages.append({'role': 'user', 'content': query})

    # Run the agent and collect the response.
    responses = bot.run(messages=messages)
    response_text = "\n".join([response['content'] for response in responses])
    return response_text
