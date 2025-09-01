# Personality-Driven NPC with LLM (Ollama + Llama 3.1 + Streamlit)

## 📝 What This Project Is About

This is my 2nd Project in "15 projects to master Conversational AI" series
This project is a simple but fun experiment: building an **NPC that talks like it has a personality**.
Instead of generic chatbot answers, the NPC stays in-character. You could provide any personality you would like and it would answer in that way.

It’s powered by **Ollama** running **Llama 3.1 locally**, so no cloud APIs or internet required.

We’ve also added a Streamlit GUI so you can chat with your NPC in a simple, game-like interface.

---

## What It Can Do

- Lock an NPC into a personality and keep responses consistent.
- Respond in a roleplay-friendly way (not just Q\&A).
- Run fully offline using Ollama.
- Built with just **Python + requests + Streamlit** — lightweight and easy to extend.

---

## How It Works

1. Player input goes through a Streamlit UI.
2. Python sends it to the Ollama API.
3. A prompt template makes sure the NPC replies in-character.
4. The dialogue history is saved in session state, so conversations feel continuous.

It’s not fancy AI agent stuff, just some zero-shot prompting plus a lightweight UI. But it works.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** (for a simple UI)
- **Requests** (to talk to Ollama’s API)
- **Ollama + Llama 3.1** (local LLM inference)

---

## 🚀 How To Run

1. Install [Ollama](https://ollama.ai).
2. Pull the model:

   ```bash
   ollama pull llama3.1
   ```

3. Install dependencies:

   ```bash
   pip install streamlit requests
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

Type something into the chatbox and the NPC will respond in character.

---

## 🧠 What I Learned

- Prompt engineering is powerful: with the right framing, you can “lock” an LLM into a believable personality.
- Streamlit makes it dead simple to throw together a prototype UI.
- Running models locally with Ollama feels way more flexible than depending on an external API.

---

## 🎮 Where It Could Go

This project could evolve into:

- NPCs for indie RPGs or text adventures.
- Storytelling bots with unique voices.
- A testbed for experimenting with memory, self-awareness, or multi-character interactions.

---

Do you want me to also **add an example prompt template** (like how you set up the “grumpy blacksmith” personality) to the README so it feels more hands-on and not just descriptive?
