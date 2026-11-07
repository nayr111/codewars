def create_phone_number(n):
    #group the integers together in the string, into a 3-3-4 pattern.
    #then, add parentheses around the first 3 chunk, and a dash between the second 3 chunk
    # and the last chunk.
    #finally, return the final result as a string.
    
    chunksize = 3
    chunks = [n[i : i + chunksize] for i in range(0, len(n), chunksize)]
    if len(chunks) > 1 and len(chunks[-1]) < chunksize:
        chunks[-2].extend(chunks.pop())
    newlist = ["".join(map(str, chunk)) for chunk in chunks] # [123 456 7890]
    intresult = f"({newlist[0]}) {newlist[1]}-{newlist[2]}" # [(123) 456-7890]
    result = "".join(intresult) # (123) 456-7890
    return result
    
