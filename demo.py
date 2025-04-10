import streamlit as st
from pipeline.prediction_pipeline import hybrid_recommendation

# Set the title and layout
st.set_page_config(page_title="Hybrid Anime Recommendation App", layout="centered")

st.title("🎯 Hybrid Anime Recommendation System")

# Input field for User ID
user_id = st.text_input("Enter User ID:", value="", help="Enter a valid numeric user ID")

# Button to generate recommendations
if st.button("Get Recommendations"):
    try:
        user_id = int(user_id)
        recommendations = hybrid_recommendation(user_id)

        if recommendations:
            st.success("Top Recommendations:")
            for idx, item in enumerate(recommendations, 1):
                st.write(f"{idx}. {item}")
        else:
            st.warning("No recommendations found for the given user ID.")
    except ValueError:
        st.error("Please enter a valid integer for User ID.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
