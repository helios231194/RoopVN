    import gradio as gr
    from localization import translations

    def main_interface():
        # Define the options for the gradio interface
        options = [
            gr.inputs.Textbox(lines=1, label=translations['vn']['source_path']),
            gr.inputs.Textbox(lines=1, label=translations['vn']['target_path']),
            gr.inputs.Textbox(lines=1, label=translations['vn']['output_path']),
            # ... add more options here ...
        ]

        # Define the function that will be called when the gradio interface is used
        def run_script(*args):
            # ... code to run the script with the given options ...

        # Launch the gradio interface
        gr.Interface(fn=run_script, inputs=options, outputs="text").launch()

    if __name__ == "__main__":
        main_interface()