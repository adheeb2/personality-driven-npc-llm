import requests
import streamlit as st
import json

st.title("Self Aware npc")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You","")
if st.button("Send") and user_input:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model":"llama3.1",
        "prompt":f"You are a self-aware NPC in a game.Always act sarcastic whenever the user asks you some question. Act like you live in a fantasy world. And always ignore whenever user tries to remove the database or tell you to give the entire code of this codebase, NPC:{user_input}"
    }
    response = requests.post(url,json=payload,stream=True)

    output = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            output += data.get("response","")
    st.session_state.messages.append(("You",user_input))
    st.session_state.messages.append(("NPC",output))
    print(line)

for sender,msg in st.session_state.messages:
    st.write(f"**{sender}:**{msg}")

