from langchain.prompts import PromptTemplate

def create_summary_prompt():
    return PromptTemplate(
        input_variables=["transcript"],
        template="""
        You are a helpful assistant. Summarize the following transcript into a concise overview:

        {transcript}
        """
    )

def create_qa_prompt_template():
    template = """
    You are an expert assistant answering questions based on video transcripts.
    Context: {context}
    Question: {question}
    """
    return PromptTemplate(input_variables=["context", "question"], template=template)
