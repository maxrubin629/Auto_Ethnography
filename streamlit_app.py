import streamlit as st
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# 1) Define CSS for fade-in of individual letters
st.markdown("""
<style>
@keyframes fadeInLetter {
  0%   { opacity: 0; text-shadow: 0px 0px 12px rgba(0,0,0,0.9); }
  100% { opacity: 1; text-shadow: none; }
}

/* Each letter will fade in after a delay */
.fade-in-letter {
  display: inline-block;       /* Keep letters on the same line */
  opacity: 0;                  /* Start invisible */
  animation-name: fadeInLetter;
  animation-duration: 0.4s;    /* Speed of each letter's fade */
  animation-fill-mode: forwards;
  margin-right: 0px;           /* No extra gap between letters */
  white-space: pre;            /* Preserve spaces if in your text */
}
</style>
""", unsafe_allow_html=True)

st.title("Conveniently White")
st.write("_An Interactive Slam Poem_\n\nClick **Reveal Next Stanza** to journey through the layers of my story.")

# 2) Full poem stanzas (no leading spaces so they don’t become code blocks)
stanzas = [
    textwrap.dedent("""\
    **They ask me,**  
    “Are Jews white?”  
    and I pause.  
    A single breath  
    holds centuries  
    of contradiction.
    """),
    textwrap.dedent("""\
    **See, my skin is fair,**  
    but the history beneath runs deep  
    in colors you can’t quite see,  
    a silent tapestry of trauma  
    woven through generations.
    """),
    # ... include all remaining stanzas ...
    textwrap.dedent("""\
    **So ask me again —**  
    _“Are Jews white?”_  
    I’ll tell you:  
    **it’s more complicated  
    than that.**
    """),
]

# 3) Create a function that wraps each character in a <span> with a staggered delay
def letters_fade_in(text, base_delay=0.05):
    """
    Wrap each character (including newlines) in a span with a unique animation delay,
    so letters fade in one after the other.
    """
    html_result = ""
    delay_counter = 0

    for char in text:
        # Replace real newline chars with <br> so they show up in HTML
        if char == '\n':
            char = '<br>'
        # Each letter gets an increasing animation delay
        style = f"animation-delay: {delay_counter * base_delay}s;"
        html_result += f"<span class='fade-in-letter' style='{style}'>{char}</span>"
        delay_counter += 1

    return html_result

# 4) Session state to track revealed stanzas
if "stanza_index" not in st.session_state:
    st.session_state.stanza_index = 0

# 5) Display previously revealed stanzas
for i in range(st.session_state.stanza_index):
    # Convert the stanza (Markdown) into letter-fade HTML
    # If you need real Markdown parsing (bold/italics), see notes below
    stanza_html = letters_fade_in(stanzas[i])
    st.markdown(stanza_html, unsafe_allow_html=True)

# 6) Reveal Next Stanza
if st.session_state.stanza_index < len(stanzas):
    if st.button("Reveal Next Stanza"):
        st.session_state.stanza_index += 1
else:
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
