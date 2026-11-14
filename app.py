import streamlit as st

# App ka title aur configuration
st.set_page_config(page_title="My Personal AI Squad", page_icon="🤖", layout="centered")

st.title("🤖 My Personal AI Squad")
st.caption("Your custom AI companion that never forgets your stories (Gurmeet, Kavya, Pyare Lal, G-4).")

# Session state to store chat history (Ye memory maintain karega)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chats ko screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Naya message input lene ke liye chat box
if prompt := st.chat_input("Apni kahani ya sawal yahan type karo..."):
    # User ka message add karo
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI ka response (Filhal ye temporary reply dega, baad mein hum isme apna AI/Memory jodenge)
    ai_response = f"Maine sun liya! Tumne kaha: '{prompt}'. Abhi main tumhari memory aur baaki agents ko isme jod raha hoon."
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
      
