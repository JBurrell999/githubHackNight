
import openai
import streamlit as st

openai.api_key = "your-openai-api-key"

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            n=1,
            stop=None
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        return f"Error: {e}"

st.title("Chatbot with OpenAI GPT")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if user_input:
    response = generate_response(user_input)
    st.write("Bot:", response)
