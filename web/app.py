# web/app.py
import streamlit as st
from core.image_generator import generate_image_from_prompt
from core.image_animator import animate_image
import os

st.set_page_config(page_title="FaeSwap: Be Who You Wanna Be")

st.title("🧝‍♀️ FaeSwap: Be Who You Wanna Be")
st.markdown("Type a fantasy identity. Generate a face. Animate it with your soul.")

prompt = st.text_input("✨ Describe your dream identity (e.g., 'hula dancer with a flower crown')")

if st.button("🎨 Generate Face"):
    image_path = generate_image_from_prompt(prompt)
    st.image(image_path, caption="Generated Identity", use_column_width=True)

    blueprint_path = "blueprint/chandra_expressions.mp4"
    output_path = "generated/animated_output.mp4"

    with st.spinner("Animating with your blueprint..."):
        animated_video = animate_image(image_path, blueprint_path, output_path)
        st.video(animated_video)

    st.success("✨ Your Fae identity is alive.")
