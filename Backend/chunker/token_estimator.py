import tiktoken

def estimate_token(text: str,model: str = "gpt-3.5-turbo") -> int:
    try:
        enc = tiktoken.encoding_for_model(model)
    
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")
    
    return len(enc.encode(text))