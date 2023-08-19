import gradio as gr

pegasus = gr.Interface.load("huggingface/google/pegasus-xsum", 
                            inputs=gr.Textbox(lines=20, placeholder="Content Here..."),
                            outputs=gr.Textbox(lines=20, placeholder="...")).queue(concurrency_count=2)

pegasus.launch(share=True)

