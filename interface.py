import gradio as gr
from model_agent import handle_query

# Define the Gradio interface.
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
            source_code = gr.Textbox(
                placeholder="Upload target source code here...",
                label="Script",
                lines=8,
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

    # Define the generator for streaming responses.
    def stream_responses(fuzzer_selection, source_code, problem_description):
        messages = []
        for token in handle_query(fuzzer_selection, source_code, problem_description, messages):
            yield token

    def clear_inputs():
        return "", "", ""

    # Set up Gradio for streaming.
    submit_button.click(
        fn=stream_responses,
        inputs=[fuzzer_selection, source_code, problem_description],
        outputs=display_window
    )
    
    clear_button.click(
        fn=clear_inputs,
        inputs=[],
        outputs=[fuzzer_selection, source_code, problem_description]
    )

    # Add CSS styling for button colors
    fuzzing_interface.css = """
    #submit-button {
        background-color: green;
        color: white;
        font-weight: bold;
    }
    """

# Launch the Gradio interface
if __name__ == "__main__":
    fuzzing_interface.launch(share=True)
