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
        "prompt":f"NPC:{user_input}"
    }
    response = requests.post(url,payload,stream=True)

    output = ""
    for line in response.iter_lines:
        if line:
            data = json.loads(line)
            output += data.get("response","")
    st.session_state.messages.append(("You",user_input))
    st.session_state.messages.append(("NPC",output))

for sender,msg in st.session_state.messages:
    st.write(f"**{sender}:**{msg}")
