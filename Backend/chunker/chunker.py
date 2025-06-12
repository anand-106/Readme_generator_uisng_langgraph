from chunker.token_estimator import estimate_token

def extract_symbols_from_ast(ast):
    symbols = []
    for folder in ast.get("structure", []):
        for file in folder.get("files", []):
            for symbol in file.get("symbols", []):
                # Add filename or path for better tracking
                symbol["file"] = file["name"]
                # Compute line count if not already
                if "lines" not in symbol:
                    symbol["lines"] = symbol["end_line"] - symbol["start_line"] + 1
                symbols.append(symbol)
    return symbols


def prepare_chunks(ast,max_call=13,max_tokens_per_call = 6000):
    all_symbols=extract_symbols_from_ast(ast)

    sorted_chunks  = sorted(all_symbols,key= lambda x:x['lines'],reverse=True)

    chunks= []
    current_chunk=[]
    current_token_estimate=0

    for symbols in sorted_chunks:

        tokens = estimate_token(symbols["raw_code"])

        if len(chunks)> max_call:
            break

        if current_token_estimate+tokens > max_tokens_per_call:
            chunks.append(current_chunk)
            current_chunk=[]
            current_token_estimate=0
        
        current_chunk.append(symbols)
        current_token_estimate += tokens

    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks