def genTextSummarizationPrompt(text: str):
    def textPrompt(t):
        return f"The text you need to summarize is: {t}"
    chats = [
        {
            "role": "system", 
            "content": "You are a master in text summarization, you need to give a concise summary of the given text. No other messages or data is allowed after you give the summarization of a text."
        }
    ]
    chats.append({
            "role": "user",
            "content": textPrompt(text)
        }
    )
    return chats
