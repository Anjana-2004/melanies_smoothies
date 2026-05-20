import streamlit as st

st.title("🍹 Melanie's Smoothies")

st.header("Welcome to our smoothie shop!")

# Add a simple form
with st.form("smoothie_form"):
    st.write("Order your favorite smoothie:")
    
    smoothie_choice = st.selectbox(
        "Choose a smoothie:",
        ["Strawberry Banana", "Mango Pineapple", "Mixed Berry", "Green Smoothie"]
    )
    
    size = st.radio(
        "Select size:",
        ["Small", "Medium", "Large"]
    )
    
    submitted = st.form_submit_button("Order Now")
    
    if submitted:
        st.success(f"Great choice! You ordered a {size} {smoothie_choice} 🎉")

st.divider()

st.write("### Our Menu")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Strawberry Banana**")
    st.write("Fresh strawberries and ripe bananas")

with col2:
    st.write("**Mango Pineapple**")
    st.write("Tropical blend with mango and pineapple")

with col3:
    st.write("**Mixed Berry**")
    st.write("Blueberries, raspberries, and blackberries")
