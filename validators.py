def validate_comment_payload(data):
    if not data:
        return "Request body missing"

    content = data.get("content", "").strip()

    if not content:
        return "Comment content cannot be empty"

    if len(content) > 500:
        return "Comment must be under 500 characters"

    return None
