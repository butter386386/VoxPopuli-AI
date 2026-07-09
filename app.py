import streamlit as st
import joblib

# Load the trained AI model we just uploaded
try:
    model = joblib.load('voxpopuli_model.pkl')
except:
    model = None

# Set up a professional website header layout
st.set_page_config(page_title="VoxPopuli AI Dashboard", layout="centered")
st.title("📊 VoxPopuli AI: App Store Intelligence Analyzer")
st.markdown("---")
st.write("This interactive system utilizes Natural Language Processing (NLP) models to automatically clean, classify, and extract developer-critical feedback trends from mobile application store user text.")

# Create the user input text field box
user_review = st.text_input("Enter a Sample Mobile App User Review Text:", "The Login screen layout is good.")

# When user clicks the analyze button
if st.button("Execute AI Sentiment Analysis Pipeline"):
    if model:
        # Run prediction
        prediction = model.predict([user_review])
        
        # Display professional metric badges based on results
        if prediction == "Positive":
            st.success(f"**AI Classification Result: {prediction}** (User Sentiment is Optimal)")
        elif prediction == "Negative":
            st.error(f"**AI Classification Result: {prediction}** (Flagged Software Optimization Needed)")
        else:
            st.warning(f"**AI Classification Result: {prediction}** (Neutral Commentary)")
    else:
        st.info("System Engine Ready. Model file connection configuration required.")
