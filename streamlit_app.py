import streamlit as st
import re
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# --- 1) DEFINE CUSTOM CSS FOR LETTER-BY-LETTER FADE-IN ---
# Each letter is placed in a <span> with an incremental animation-delay
st.markdown(
    """
    <style>
    @keyframes fadeInLetter {
      from {
        opacity: 0; 
        text-shadow: 0 0 8px rgba(0,0,0,0.8);
      }
      to {
        opacity: 1; 
        text-shadow: none;
      }
    }

    .letter-fade {
      display: inline-block;
      opacity: 0;
      animation: fadeInLetter 0.6s forwards; /* how long each letter fades */
      margin-right: 0; /* no extra spacing */
      white-space: pre-wrap; /* preserve line breaks/spaces */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 2) POEM TEXT (AS PLAIN TEXT) ---
# Indentation can cause markdown code blocks, so make sure there's no leading spaces on each line
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

**Imagine me, seven, in LA,**  
minding my own business,  
kippah balanced on my head  
like a crown  
unashamed,  
unaware  
of the cost  
of visibility.

**Until words slice the air—**  
slurs hurled  
like rocks,  
sharp enough  
to carve doubt  
into a child’s courage.

... (include all remaining lines) ...

**So ask me again —**  
_“Are Jews white?”_  
I’ll tell you:  
**it’s more complicated  
than that.**
""")

# --- 3) NAIVE MARKDOWN SUPPORT (BOLD & ITALICS ONLY) ---
# This quick parse ensures "**bold**" -> <b>bold</b> and "_italics_" -> <i>italics</i>.
# If your text has underscores for emphasis, it will become <i>.
def naive_md_to_html(text: str) -> str:
    # Replace **bold** with <b>bold</b>
    text = re.sub(r"\\*\\*(.*?)\\*\\*", r"<b>\\1</b>", text)
    # Replace _italics_ with <i>italics</i>
    text = re.sub(r"_(.*?)_", r"<i>\\1</i>", text)
    # Replace line breaks (\n) with <br>
    text = text.replace("\\n", "<br>")
    return text

# --- 4) WRAP EACH CHARACTER IN SPANS WITH A UNIQUE DELAY ---
def letter_by_letter_fade(html_text: str, delay_increment: float = 0.02) -> str:
    """
    Takes an HTML string and wraps each character (except <, > inside tags) in a
    <span class='letter-fade' style='animation-delay:Xs'> so they fade in sequentially.
    """
    output = []
    delay = 0.0
    in_tag = False

    for char in html_text:
        if char == "<":
            in_tag = True
            output.append(char)
        elif char == ">":
            in_tag = False
            output.append(char)
        else:
            if in_tag:
                # inside an HTML tag (like <b>), don't wrap in a <span>
                output.append(char)
            else:
                # actual character content => wrap in fade span
                styled_span = (
                    f"<span class='letter-fade' style='animation-delay:{delay:.2f}s'>"
                    f"{char}</span>"
                )
                output.append(styled_span)
                delay += delay_increment

    return "".join(output)

# --- 5) BUILD THE FINAL HTML ---
# 1) naive parse of bold/italics
poem_html = naive_md_to_html(poem)
# 2) wrap each character
poem_html = letter_by_letter_fade(poem_html)

# --- 6) LAYOUT ---
st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An Interactive Slam Poem_\n\nClick **Begin Poem** to see it unfold.")

if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

if st.button("Begin Poem"):
    st.session_state.show_poem = True

if st.session_state.show_poem:
    # Single pass: render the entire poem at once
    st.markdown(poem_html, unsafe_allow_html=True)
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
