import streamlit as st

st.set_page_config(page_title="Conveniently White: An Interactive Slam Poem", layout="centered")

st.title("Conveniently White")
st.write("_An Interactive Slam Poem_\n\nPress **Spacebar** or click **Reveal Next Stanza** to journey through the layers of my story.")

stanzas = [
    # [Your full list of stanzas here, unchanged]
]

# Initialize stanza index
if "stanza_index" not in st.session_state:
    st.session_state.stanza_index = 0

# JavaScript to detect Spacebar press
spacebar_script = """
<script>
document.addEventListener('keydown', function(e) {
    if (e.code === 'Space') {
        const buttons = parent.document.querySelectorAll('button');
        buttons.forEach(btn => {
            if (btn.innerText === 'Reveal Next Stanza') {
                btn.click();
            }
        });
    }
});
</script>
"""

# Display stanzas up to current index
for i in range(st.session_state.stanza_index):
    st.markdown(stanzas[i])

# Button placed after current stanza
if st.session_state.stanza_index < len(stanzas):
    if st.button("Reveal Next Stanza"):
        st.session_state.stanza_index += 1
        st.rerun()
else:
    st.write("You've reached the end of the poem. Thank you for journeying with me!")

# Inject JavaScript to listen for spacebar
st.components.v1.html(spacebar_script, height=0, width=0)
