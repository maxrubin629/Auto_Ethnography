import streamlit as st
import re
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# 1) Define your entire poem as plain text with minimal indentation
poem = textwrap.dedent("""\
**They ask me,**  
“Are Jews white?”  
and I pause.  
A single breath  
holds centuries  
of contradiction.

**See, my skin is fair,**  
but the history beneath runs deep  
in colors you can’t quite see,  
a silent tapestry of trauma  
woven through generations.

# ... (paste all your lines exactly, no leading spaces)...

**So ask me again —**  
_“Are Jews white?”_  
I’ll tell you:  
**it’s more complicated  
than that.**
""")

# 2) Custom CSS for letter fade-in from shadow
# Each letter uses a different 'animation-delay' so they appear sequentially.
st.markdown("""
<style>
@keyframes fadeInLetter {
    0%   { opacity: 0; text-shadow: 0px 0px 10px rgba(0,0,0,0.9); }
    100% { opacity: 1; text-shadow: none; }
}

/* Each letter gets an inline 'animation-delay' via style='' in our code below */
.letter-fade {
    display: inline-block;
    opacity: 0;
    animation-name: fadeInLetter;
    animation-duration: 0.7s; /* how long each letter's fade lasts */
    animation-fill-mode: forwards;
    margin: 0;
    white-space: pre-wrap; /* preserve newlines/spaces */
}
</style>
""", unsafe_allow_html=True)

# 3) Simple "naive" bold/italics converter:
def naive_markdown_to_html(text: str) -> str:
    """
    Converts **bold** to <b></b> and _italics_ to <i></i>.
    Replaces newlines with <br> so it visually breaks lines.
    This won't parse advanced Markdown features like # headings, lists, etc.
    """
    # convert **bold** => <b></b>
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    # convert _italics_ => <i></i>
    text = re.sub(r"_(.*?)_", r"<i>\1</i>", text)
    # replace literal newlines with <br>
    text = text.replace('\n', '<br>')
    return text

# 4) Wrap each visible character in a <span> with an incrementing animation-delay
def letter_fade_html(html_text: str, delay_increment: float = 0.015) -> str:
    """
    For each character outside of tags, wrap in <span class='letter-fade' style='animation-delay:Xs'>.
    This way, letters fade in sequentially.
    """
    output = []
    delay = 0.0
    in_tag = False

    for char in html_text:
        if char == '<':
            in_tag = True
            output.append(char)
        elif char == '>':
            in_tag = False
            output.append(char)
        else:
            if in_tag:
                # inside HTML tag (<b>, </b>, etc.), just append directly
                output.append(char)
            else:
                # visible character => wrap with fade
                letter_span = (
                    f"<span class='letter-fade' style='animation-delay:{delay:.2f}s'>{char}</span>"
                )
                output.append(letter_span)
                delay += delay_increment

    return "".join(output)

# 5) Convert poem from naive Markdown => HTML => per-letter spans
poem_html = naive_markdown_to_html(poem)
poem_html = letter_fade_html(poem_html)

# 6) Show UI
st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An Interactive Slam Poem_\n\nClick **Begin Poem** to see it gently emerge in letters from shadows.")

if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

if st.button("Begin Poem"):
    st.session_state.show_poem = True

if st.session_state.show_poem:
    # display entire poem at once, each character with a staged fade
    st.markdown(poem_html, unsafe_allow_html=True)
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
