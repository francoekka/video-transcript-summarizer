import gradio as gr
from transcriptSummerizer.helpers import get_transcript, process, chunk_transcript
from transcriptSummerizer.config import initialize_gemma_llm, setup_embedding_model
from transcriptSummerizer.prompts import create_summary_prompt, create_qa_prompt_template
from transcriptSummerizer.chains import create_summary_chain, create_qa_chain
from transcriptSummerizer.vectorstore import create_faiss_index, perform_similarity_search

processed_transcript = ""

def summarize_video(video_url):
    global processed_transcript
    transcript = get_transcript(video_url)
    if not transcript:
        return "No transcript available."
    processed_transcript = process(transcript)

    llm = initialize_gemma_llm()
    summary_prompt = create_summary_prompt()
    summary_chain = create_summary_chain(llm, summary_prompt)
    return summary_chain.invoke({"transcript": processed_transcript})

def answer_question(video_url, user_question):
    global processed_transcript
    if not processed_transcript:
        transcript = get_transcript(video_url)
        if not transcript:
            return "No transcript available."
        processed_transcript = process(transcript)

    chunks = chunk_transcript(processed_transcript)
    embedding_model = setup_embedding_model()
    faiss_index = create_faiss_index(chunks, embedding_model)

    llm = initialize_gemma_llm()
    qa_prompt = create_qa_prompt_template()
    qa_chain = create_qa_chain(llm, qa_prompt)
    context = perform_similarity_search(faiss_index, user_question)
    return qa_chain.invoke({"context": context, "question": user_question})

with gr.Blocks() as interface:
    gr.Markdown("<h2 style='text-align: center;'>YouTube Video Summarizer and Q&A</h2>")
    video_url = gr.Textbox(label="YouTube Video URL")
    summary_output = gr.Textbox(label="Video Summary", lines=5)
    question_input = gr.Textbox(label="Ask a Question")
    answer_output = gr.Textbox(label="Answer", lines=5)
    summarize_btn = gr.Button("Summarize Video")
    question_btn = gr.Button("Ask a Question")

    summarize_btn.click(summarize_video, inputs=video_url, outputs=summary_output)
    question_btn.click(answer_question, inputs=[video_url, question_input], outputs=answer_output)

interface.launch(server_name="0.0.0.0", server_port=7860)
