import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="UCase_004", page_icon="📊")
st.markdown("# UCase_004")
st.sidebar.header("UCase_004")

st.title("Manufacturing: Use Case #4")
st.subheader("Fanuc Robot Assistant")

st.write("📄 Enter an alarm code for Fanuc robots, and GPT will provide troubleshooting steps!")

# Use API key from session state
if "api_key" not in st.session_state:
    st.error("API key is missing. Please configure it in the main page.")
else:
    openai_api_key = st.session_state.api_key
    client = OpenAI(api_key=openai_api_key)

    # Ask for an alarm code
    alarm_code = st.text_area("Describe the Robot Alarm Code", placeholder="Enter the alarm code (e.g., SRVO-023)...")

    if alarm_code:
        # Generate a response using OpenAI API
        question = f"Can you give me the explanation and road map to troubleshoot the Robot alarm code: {alarm_code}"
        messages = [{"role": "user", "content": question}]

        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )

        # Display the response
        st.write_stream(stream)
