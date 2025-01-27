from llama_cpp import Llama


def createModel():
    llm = Llama(model_path="./model/Llama-3-8B-Instruct-32k-v0.1.Q4_K_M.gguf")
    return llm


def generate_response(llm, text):
    response = llm(
        text,
        max_tokens=1094,
        temperature=0.3,
    )
    return response["choices"][0]["text"]

if __name__ == "__main__":
    llm = createModel()
    x = generate_response(llm, "What is the capital of India")
    print(x)
