from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

def createModel(api_key):
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=api_key
    )
    return gemini_llm

def generate_response(llm , text):
    ai_msg = llm.invoke(text)
    return ai_msg.content

