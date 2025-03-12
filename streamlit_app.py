import streamlit as st
import re
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# Define the poem as plain text with minimal indentation
poem = textwrap.dedent("""\
**They ask me,**  
"Are Jews white?"  
and I pause.  
A single breath  
holds centuries  
of contradiction.

**See, my skin is fair,**  
but the history beneath runs deep  
in colors you can't quite see,  
a silent tapestry of trauma  
woven through generations.

**So ask me again —**  
*"Are Jews white?"*  
I'll tell you:  
**it's more complicated  
than that.**
""")

# Custom CSS for letter fade-in animation
st.markdown("""
<style>
@keyframes fadeInLetter {
    0%   { opacity: 0; text-shadow: 0px 0px 10px rgba(0,0,0,0.9); }
    100% { opacity: 1; text-shadow: none; }
}

.letter-fade {
    display: inline-block;
    opacity: 0;
    animation-name: fadeInLetter;
    animation-duration: 0.7s;
    animation-fill-mode: forwards;
    margin: 0;
    white-space: pre-wrap;
}

.poem-container {
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

def convert_markdown_to_html(text):
    """Convert markdown bold and italic to HTML tags"""
    # Convert **bold** to <strong>bold</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Convert *italic* to <em>italic</em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Convert newlines to <br>
    text = text.replace('\n', '<br>')
    return text

def create_letter_animation_html(html_text, delay_increment=0.015):
    """
    Wraps each visible character with animation spans while preserving HTML tags
    """
    result = []
    delay = 0.0
    in_tag = False
    
    for char in html_text:
        if char == '<':
            in_tag = True
            result.append(char)
        elif char == '>':
            in_tag = False
            result.append(char)
        elif in_tag:
            # Inside an HTML tag, don't animate
            result.append(char)
        else:
            # Visible character, add animation
            if char.strip():  # If not just whitespace
                span = f'<span class="letter-fade" style="animation-delay:{delay:.3f}s">{char}</span>'
                result.append(span)
                delay += delay_increment
            else:
                # Preserve whitespace
                result.append(char)
    
    return ''.join(result)

# UI Structure
st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An Interactive Slam Poem_\n\nClick **Begin Poem** to see it gently emerge letter by letter from shadows.")

# Initialize session state
if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

# Button to trigger poem display
if st.button("Begin Poem"):
    st.session_state.show_poem = True

# Display the animated poem when triggered
if st.session_state.show_poem:
    # Process the poem text
    html_poem = convert_markdown_to_html(poem)
    animated_poem = create_letter_animation_html(html_poem)
    
    # Display in a container
    st.markdown(
        f'<div class="poem-container">{animated_poem}</div>',
        unsafe_allow_html=True
    )
    
    # Show completion message
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
