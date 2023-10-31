import gradio as gr
import os
from user_interface import create_demo
from logic import enable_api_box, add_text, generate_response, render_file

demo, chatbot, show_img, txt, submit_btn, btn = create_demo()

with demo:

    btn.upload(render_file, inputs=[btn], outputs=[show_img])

    submit_btn.click(add_text, inputs=[chatbot, txt], outputs=[chatbot], queue=False).\
        success(generate_response, inputs=[chatbot, txt, btn], outputs=[chatbot, txt]).\
        success(render_file, inputs=[btn], outputs=[show_img])

if __name__ == "__main__":
    os.environ['OPENAI_API_KEY'] = "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"
    demo.launch()
