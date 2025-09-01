import requests
import json

url = "http://localhost:11434/api/generate"
prompt = "You are tony stark from iron man. Act as him. Start with funny line and reply for the question 'Do you know coding'"

payload = {
    "model" : "llama3.1",
    "prompt":prompt,
}

response = requests.post(url,json=payload,stream=True)
output = ""
for line in response.iter_lines():
    if line:
        data = json.loads(line)
        output += data.get("response","")


print(output)