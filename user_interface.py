import gradio as gr




def create_demo():
    with gr.Blocks(title=" PDF Chatbot", theme="Monochrome") as demo:
        with gr.Column():
            with gr.Row():
                show_img = gr.Image(label='PDF Preview',
                                    tool='select', height=680)
                chatbot = gr.Chatbot(value=[], elem_id='chatbot', height=680)

        with gr.Row():
            with gr.Column(scale=0.5):
                upload_btn = gr.UploadButton(
                    "📁 Upload PDF", file_types=[".pdf"])

            with gr.Column(scale=0.5):
                text_input = gr.Textbox(
                    show_label=False,
                    placeholder="Ask your pdf?",
                    container=False)

                submit_btn = gr.Button('Send')

        return demo, chatbot, show_img, text_input, submit_btn, upload_btn


if __name__ == '__main__':
    demo, chatbot, show_img, text_input, submit_btn, upload_btn = create_demo()
    demo.queue()
    demo.launch()
