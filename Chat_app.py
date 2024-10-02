import streamlit
import numpy
# Face icon
# message =  streamlit.chat_message("assistant")
# Write Hello into the Face Bar
# streamlit.write("Hello")
# Bar chart
# streamlit.bar_chart(numpy.random.randn(30,3))
# prompt = streamlit.chat_input("Say somthing")

# if prompt:
    # streamlit.write(f"User: {prompt}")
streamlit.title("Echo Bot")

# Initialize chat history
if "messages" not in streamlit.session_state:
    streamlit.session_state.messages = []
# React to user input
for mess in streamlit.session_state.messages:
    with streamlit.chat_message(mess["role"]):
        streamlit.markdown(mess["content"])

if prompt := streamlit.chat_input("What is up?"):

    # Display user message in chat message container
    with streamlit.chat_message("user"):
        streamlit.markdown(prompt)

    # Add user message to chat history
    streamlit.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"

# Display assistant response in chat message container
with streamlit.chat_message("assistant"):
    streamlit.markdown(response)

# Add assistant response to chat history
streamlit.session_state.messages.append({"role": "assistant", "content": response})
