import streamlit as st
import re

st.set_page_config(page_title=\"Conveniently White\", layout=\"centered\")

# Minimal CSS
st.markdown(\"\"\"\n<style>\n@keyframes fadeInLetter {\n  from { opacity: 0; text-shadow: 0 0 8px rgba(0,0,0,0.8); }\n  to   { opacity: 1; text-shadow: none; }\n}\n.letter-fade {\n  display: inline-block;\n  opacity: 0;\n  animation: fadeInLetter 0.6s forwards;\n}\n</style>\n\"\"\", unsafe_allow_html=True)

raw_poem = \"\"\"**Bold** and normal text <some weird> stuff\nLine 2\nLine 3\n\"\"\"

# Basic parse for bold/italics
def naive_md_to_html(text):
    text = re.sub(r'\\*\\*(.*?)\\*\\*', r'<b>\\1</b>', text)
    text = re.sub(r'_(.*?)_', r'<i>\\1</i>', text)
    text = text.replace('\\n', '<br>')
    return text

parsed_html = naive_md_to_html(raw_poem)

def letter_by_letter_fade(full_html: str, delay_increment=0.03) -> str:
    out = []
    delay = 0.0
    in_tag = False
    for char in full_html:
        if char == '<':
            in_tag = True
            out.append(char)
        elif char == '>':
            in_tag = False
            out.append(char)
        else:
            if in_tag:
                # Inside HTML tag
                out.append(char)
            else:
                # wrap visible text
                out.append(f\"<span class='letter-fade' style='animation-delay:{delay:.2f}s'>{char}</span>\")
                delay += delay_increment
    return ''.join(out)

final_html = letter_by_letter_fade(parsed_html)
st.markdown(final_html, unsafe_allow_html=True)
