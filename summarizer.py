from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def chunk_text(text, max_tokens=1024):
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    chunks.append(current_chunk.strip())
    return chunks


def summarize_text(text):
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        summary = summarizer(chunk, max_length=130,
                             min_length=30, do_sample=False)
        summaries.append(summary[0]["summary_text"])

    return "\n".join(summaries)
