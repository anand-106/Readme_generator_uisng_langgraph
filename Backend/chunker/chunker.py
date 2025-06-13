from chunker.token_estimator import estimate_token
import json

def extract_symbols_from_ast(ast):
    symbols = []
    for folder in ast.get("structure", []):
        for file in folder.get("files", []):
            for symbol in file.get("symbols", []):
                symbol["file"] = file["name"]
                if "lines" not in symbol:
                    symbol["lines"] = symbol["end_line"] - symbol["start_line"] + 1
                symbols.append(symbol)
    return symbols

def prepare_chunks(ast, max_call=13, max_tokens_per_call=6000):
    all_symbols = extract_symbols_from_ast(ast)
    sorted_chunks = sorted(all_symbols, key=lambda x: x['lines'], reverse=True)

    chunks = []
    current_chunk = []
    current_token_estimate = 0

    for symbol in sorted_chunks:
        tokens = estimate_token(symbol.get("raw_code"))

        # If symbol alone exceeds token limit, add it as its own chunk
        if tokens > max_tokens_per_call:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
                current_token_estimate = 0
            chunks.append([symbol])
            if len(chunks) >= max_call:
                break
            continue

        # If current chunk will overflow, push it and start new one
        if current_token_estimate + tokens > max_tokens_per_call:
            if current_chunk:
                chunks.append(current_chunk)
                if len(chunks) >= max_call:
                    break
                current_chunk = []
                current_token_estimate = 0

        current_chunk.append(symbol)
        current_token_estimate += tokens

    # Append remaining chunk if not empty and max_call not reached
    if current_chunk and len(chunks) < max_call:
        chunks.append(current_chunk)
    
    try:
        file = open("C:/Users/gamin/Documents/projects/Readme_generator_uisng_langgraph/Backend/chunker/extracted_chunks.json",'w',encoding='utf-8')
        json.dump(chunks,file,indent=2,ensure_ascii=False)
        print(f'Successfully created {len(chunks)} chunks')
    except Exception as e:
        print(e)

    return chunks
