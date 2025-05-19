from openai import OpenAI
from fastapi import FastAPI
import promptGen
import secrets
import json
from pydantic import BaseModel, Field

app = FastAPI()

class msg(BaseModel):
    message: str

def get_completion(prompt, model=secrets.model):
    client = OpenAI(base_url=secrets.base_url, api_key=secrets.api_key)
    messages = [{"role": "user", "content": str(prompt)}]
    ans = ""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    ans = response.choices[0].message.content
    return ans

@app.post("/summarize")
def startSummarization(Msg : msg):
    prompt = promptGen.genTextSummarizationPrompt(Msg.message)
    result = get_completion(prompt)
    return {"msg": result}

if __name__ == '__main__':
    print("Please input the filename of the text file you wish to summarize(e.g Example.txt):")
    filename = input()
    while True:
        try:
            with open(f'{filename}', 'r', encoding='utf-8') as f:
                content = f.read()
            result = startSummarization(content)
            print(result)
            break
        except:
            print("No such file, please try again.")
            filename = input()
    