import gradio as gr

# Define the interface layout
with gr.Blocks() as fuzzing_interface:
    gr.Markdown("# AI Fuzzing Expert")
    
    # Main layout: Display Window on the left and Suggested Input on the right
    with gr.Row():
        # Left side: Display Window
        with gr.Column(scale=2):
            display_window = gr.Textbox(
                placeholder="Display of all inputs and responses here...",
                lines=24,  # Increase the size of the display window
                interactive=False,
                label="Answers Display Window",
                
            )
        
        # Right side: Suggested Input
        with gr.Column(scale=1):
            fuzzer_selection = gr.Dropdown(
                choices=["AFL++", "libFuzzer", "Honggfuzz", "Other"],
                label="Fuzzer Selection",
                interactive=True
            )
            target_path = gr.Textbox(
                placeholder="Path to target program...",
                label="Target Path"
            )
            question_type = gr.Dropdown(
                choices=[
                    "Setup",
                    "Start and Stop",
                    "Parameters",
                    "How to get feedback",
                    "Find crashes",
                    "Other"
                ],
                value="Setup",
                label="Type of Questions",
                interactive=True
            )
            problem_description = gr.Textbox(
                placeholder="Detailed description of your problem...",
                label="Specific Problem Description",
                lines=8,
                
            )
            # Buttons below the Suggested Input fields
            with gr.Row():
                submit_button = gr.Button("Submit", elem_id="submit-button")
                clear_button = gr.Button("Empty")

    # Custom Input Box Section (below the Display Window, with buttons at the end of the text box)
    with gr.Column():
        custom_input = gr.Textbox(
            placeholder="Ask a custom question here...",
            label="Custom Input Box",
            lines=6,
            scale=3,  # Make it wider
            
        )
        # Submit and Empty buttons horizontally aligned with the input box
        with gr.Row():
            custom_submit_button = gr.Button("Submit", elem_id="custom-submit-button", scale=1)
            custom_clear_button = gr.Button("Empty", scale=1)
        
    new_chat_button = gr.Button("New Chat", elem_id="new-chat-button")

# Add CSS styling for button colors
fuzzing_interface.css = """
#new-chat-button {
    background-color: red;
    color: white;
    font-weight: bold;
}
#submit-button {
    background-color: green;
    color: white;
    font-weight: bold;
}
#custom-submit-button {
    background-color: green;
    color: white;
    font-weight: bold;
}

"""

# Launch the interface
fuzzing_interface.launch()