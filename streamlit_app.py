import streamlit as st
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

# Custom CSS for letter fade-in effect using Streamlit's built-in markdown capabilities
st.markdown("""
<style>
.poem-container {
    max-width: 600px;
    margin: 0 auto;
}

/* Animation for the entire poem */
@keyframes fadeIn {
    from { opacity: 0; text-shadow: 0px 0px 10px rgba(0,0,0,0.9); }
    to { opacity: 1; text-shadow: none; }
}

.fade-in {
    opacity: 0;
    animation: fadeIn 3s ease-in-out forwards;
}

/* Staggered animations for poem sections */
.stanza {
    opacity: 0;
}

.stanza-1 { animation: fadeIn 2s ease-in-out 0.5s forwards; }
.stanza-2 { animation: fadeIn 2s ease-in-out 2.5s forwards; }
.stanza-3 { animation: fadeIn 2s ease-in-out 4.5s forwards; }
</style>
""", unsafe_allow_html=True)

# UI Structure
st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An Interactive Slam Poem_\n\nClick **Begin Poem** to see it gently emerge from shadows.")

# Initialize session state
if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

# Button to trigger poem display
if st.button("Begin Poem"):
    st.session_state.show_poem = True

# Display poem with staggered animation when triggered
if st.session_state.show_poem:
    # Split poem into stanzas for staggered animation
    stanzas = poem.split("\n\n")
    
    html = '<div class="poem-container">'
    for i, stanza in enumerate(stanzas):
        # Replace markdown with HTML
        stanza_html = stanza.replace("**", "<strong>").replace("**", "</strong>")
        stanza_html = stanza_html.replace("*", "<em>").replace("*", "</em>")
        stanza_html = stanza_html.replace("\n", "<br>")
        
        # Add stanza with appropriate animation class
        html += f'<div class="stanza stanza-{i+1}">{stanza_html}</div><br>'
    
    html += '</div>'
    
    # Display the poem
    st.markdown(html, unsafe_allow_html=True)
    
    # Add final message after a delay using empty space and container
    final_message = st.empty()
    import time
    time.sleep(6.5)  # Wait for animations to complete
    final_message.write("You've reached the end of the poem. Thank you for journeying with me!")
