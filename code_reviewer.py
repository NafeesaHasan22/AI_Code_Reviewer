import streamlit as st
import google.generativeai as genai

# Set up Google API
genai.configure(api_key="xxxxxxxxxxxxxx")

def review_code(user_code):
    """Send the user's code to Google AI's PaLM API for bug detection and fixes"""
    prompt = f"""
    Review the following Python code, find potential bugs or improvements, and suggest a corrected version:
    
    ```python
    {user_code}
    ```
    
    Provide a detailed bug report and an improved version of the code.
    """
    
    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash-exp")  
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🔍 AI-Powered Python Code Reviewer")

st.write("Submit your Python code below for automatic bug detection and fixes.")

# Code Input Box
user_code = st.text_area("Enter your Python code here:", height=250)

# Submit Button
if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing your code..."):
            feedback = review_code(user_code)
        
        # Display Results
        st.subheader("🛠 Bug Report & Fix Suggestions")
        st.write(feedback)
    else:
        st.warning("Please enter some Python code before submitting!")
