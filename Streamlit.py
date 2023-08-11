import streamlit as st
import subprocess

def main():
    st.title("Food Recommendation System")

    if "page" not in st.session_state:
        st.session_state.page = "welcome"

    if st.session_state.page == "welcome":
        welcome()
    elif st.session_state.page == "preferences":
        preferences()

def welcome():
    st.write("Welcome to our Food Recommendation System!")
    if st.button("Start"):
        st.session_state.page = "preferences"

def preferences():
    st.title("Food Preferences")
    st.header("Select Your Preferences")

    preference = st.radio("Select your preference:", ("Veg", "Non-Veg"))

    st.header("Disease Restrictions")
    disease_options = ["None", "Diabetes", "Lactose Intolerant", "Obesity", "High Blood Pressure"]
    disease_restriction = st.radio("Select disease restriction:", disease_options)

    if st.button("Get Recommendations"):
        st.session_state.page = "recommendations"
        # Run the Colab notebook using subprocess
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "C:\\Users\\HP\\Documents\\3rdSEM\\Intel_openAPI\\food.py"])

if __name__ == "__main__":
    main()
