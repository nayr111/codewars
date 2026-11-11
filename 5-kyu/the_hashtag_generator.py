def generate_hashtag(s):
    words = s.split()
    if not words:
        return False
    hashtag_body = "".join([word.capitalize() for word in words])
    result = f"#{hashtag_body}"
    if len(result) > 140:
        return False
    return result
    
