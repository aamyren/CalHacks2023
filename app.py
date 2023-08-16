from llama_index import (
    SimpleDirectoryReader,
    GPTVectorStoreIndex,
    LLMPredictor,
    PromptHelper,
)
from langchain.chat_models import ChatOpenAI as openai
import gradio as gr

# --- Important note ---
# Before running the app.py, run in terminal: export OPENAI_API_KEY=""
# With your openai api key inside the quotations

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 1
    chunk_size_limit = 600
    prompt_helper = PromptHelper(
        max_input_size,
        num_outputs,
        max_chunk_overlap,
        chunk_size_limit=chunk_size_limit,
    )

    llm_predictor = LLMPredictor(
        llm=openai(temperature=0.7, model_name="gpt-4.0613", max_tokens=num_outputs)
    )
    documents = SimpleDirectoryReader(directory_path, num_files_limit=1).load_data()
    index = GPTVectorStoreIndex.from_documents(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )
    index.storage_context.persist("index.json")

    return index


def chatbot(input_text):
    # rebuild storage context
    index.storage_context.persist("index.json")
    
    query_engine = index.as_query_engine()
    # set up prompt for the chatbot
    response = query_engine.query(
        """The document containes posts scraped from reddit and their comments regarding different stocks. There is title, URL, post content, comment, and timestamp information. Please refer to the documents provided to answer questions in a detailed manner about user sentiments regarding the stocks. Unless otherwise specified, assume the user is asking about recent discussions (within one week)"""
        + input_text
    )
    return response.response

# set up the chatbot interface
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.components.Textbox(lines=7, label="Ask me anything!"),
    description="I read recent reddit stock discussions so you don't have to ^ ̫^♡ Currently supported stocks are AAPL, AMZN, NCDA, PFE, TLSA. I do better when questions are more specific (ie including date/times) ᵔᵕᵔ",
    outputs="text",
    title="[̲̅$̲̅(̲̅▀̿Ĺ̯▀̿ ̿)̲̅$̲̅] Reddit stock chatbot ˊᵕˋ",
)

# set input directory, in this case "demo-data" can be changed to "generated_docs"
index = construct_index("demo-data")
# launch app
iface.launch(share=True)
