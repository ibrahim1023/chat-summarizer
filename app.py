import gradio as gr
from summarizer import summarize_text


def summarize_from_textbox(text):
    return summarize_text(text)


def summarize_from_file(file):
    if file is None:
        return "Please upload a .txt file"
    with open(file.name, "r") as f:
        content = f.read()
    return summarize_text(content)


with gr.Blocks() as demo:
    gr.Markdown(
        "# 💬 Chat Summarizer\nPaste your chat or upload a `.txt` file to get a summary.")

    with gr.Tab("📋 Paste Chat"):
        input_text = gr.Textbox(
            label="Paste chat here", lines=15, placeholder="User: Hi...\nBot: Hello...")
        output_summary1 = gr.Textbox(label="Summary", lines=10)
        summarize_btn1 = gr.Button("Summarize")
        summarize_btn1.click(fn=summarize_from_textbox,
                             inputs=input_text, outputs=output_summary1)

    with gr.Tab("📂 Upload File"):
        input_file = gr.File(label="Upload .txt file")
        output_summary2 = gr.Textbox(label="Summary", lines=10)
        summarize_btn2 = gr.Button("Summarize")
        summarize_btn2.click(fn=summarize_from_file,
                             inputs=input_file, outputs=output_summary2)

demo.launch()
