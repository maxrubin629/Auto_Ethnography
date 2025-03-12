import streamlit as st
import markdown
from markdown.extensions.nl2br import Nl2BrExtension
import time

st.set_page_config(page_title="Conveniently White", layout="centered")

# CSS for fade-in shadow animation on each stanza
st.markdown("""
<style>
@keyframes fadeInShadow {
    from { opacity: 0; text-shadow: 0 0 10px rgba(0,0,0,0.9); }
    to   { opacity: 1; text-shadow: none; }
}

.fade-in-shadow {
    animation: fadeInShadow 2s ease forwards;
    opacity: 0;
    font-size:18px;
    line-height:1.6;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An Interactive Slam Poem_")
st.write("Click **Begin Poem** to experience it unfold.")

# Your full poem as a list of stanzas
stanzas = poem.strip().split("\n\n")

# Session state initialization
if 'started' not in st.session_state:
    st.session_state.started = False

if st.button("Begin Poem"):
    st.session_state.started = True

if st.session_state.get("started", False):
    placeholder = st.empty()
    displayed = ""

    for stanza in poem.split('\n\n'):
        stanza_html = markdown.markdown(stanza, extensions=[Nl2BrExtension()])
        # Wrap stanza in div for fade-in shadow effect
        wrapped_html = f'<div class="fade-in-shadow">{stanza_html}</div>'

        # Stream character-by-character
        displayed = ""
        for char in stanza_html:
            displayed += char
            placeholder.markdown(displayed, unsafe_allow_html=True)
            time.sleep(0.002)  # adjust speed here

        # Keep revealed stanzas above
        st.markdown(f'<div class="fade-in-shadow">{stanza_html}</div>', unsafe_allow_html=True)
        placeholder.empty()  # clear streaming placeholder for next stanza

    st.write("You've reached the end of the poem. Thank you for journeying with me!")
