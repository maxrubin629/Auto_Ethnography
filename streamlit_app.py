import streamlit as st
import re
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# Define the poem as plain text with minimal indentation
poem = textwrap.dedent("""**They ask me,**
"Are Jews white?"
and I pause.
A single question
holds centuries
of contradiction.

**See, my skin is fair,**
but the history beneath runs deep
in colors you can't quite see,
a silent tapestry of trauma
woven through generations.

**Imagine me, age six,**
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
into a child's courage.

**My father knew this pain**
on Philadelphia streets,
swastikas scratched into his car,
his body bruised by fists,
scars carried quietly,
a trauma so deep
it only speaks in whispers —
or not at all.

**His grandparents fled Ukraine**
to escape the shadow
of pogroms,
anti-Jewish violence,
hate-filled riots,
stories silenced
by pain too raw
to speak aloud,
ghosts whisper
in half-forgotten Yiddish sighs.

**My mother's family lived in Morocco for centuries,**
skin much darker than mine,
generations born into languages older than borders,
until Nazis reached Casablanca streets,
signs posted on synagogues asking for names
and numbers,
listing Jews like livestock.

**They fled poverty,**
fear, and hunger,
crossed oceans to Oklahoma,
where children pawed my grandmother's curls
literally searching for horns,
hooves,
tails —
for devils their parents swore
Jews must be.

**I have her voice recorded,**
telling me softly,
how strange it felt
to have her humanity questioned
by curious fingers,
innocent and cruel
in ignorance.

**Yet, they say we're white —**
conveniently white,
when hate needs justification,
when trauma needs erasure,
when history needs rewriting,
as if skin alone defines our story,
as if violence checks melanin
before it strikes.

**I grew up in LA,**
went to school behind bulletproof glass doors,
became friends with security guards,
learned safety drills
as easily as prayers,
stood quietly
as bomb squads detonated
the threats that waited
on bus-stop benches right outside my classroom.

**I remember that one time**
I hurriedly locked a bathroom stall,
feet tucked onto porcelain
to hide blinking Skechers
from some angry man,
banging on doors trying to get in.
I heard he had a knife.

**So, at seven I learned,**
I learned what survival means —
a silent breath,
an invisible heartbeat

*SHHHHH!*

**Trips to coffee shops ended**
with strangers spitting
lectures about *"The Jews"*
at children who dared to exist
who dared to wear their faith visibly,
so I learned
to tuck mine away,
only safe within walls
that became increasingly thin.

**We went on a field trip**
to the Museum of Tolerance
and counted swastikas carved
on walls.
We listened to survivors speak,
heard their warnings—
voices trembling,
urging us
to remember
what the world would rather forget.

**And we did remember,**
but the world has amnesia.

**Because today,**
I see Jew-hatred
in Los Angeles,
around the world,
hate exploding openly
in the streets we once believed were safe.
*"Activism,"* they call it—
Yes, sometimes it is,
but sometimes it's a mask,
because I recognize the whispers
of ancestors
crying out from Ukrainian mass-graves,
from Moroccan cemeteries,
from Philadelphia backroads.

**They ask again,**
"Are Jews white?"

**Yes. No. Both. Neither.**
My whiteness
is conditional,
a temporary badge
stripped away
when convenient
to hate me openly.

**My whiteness is irrelevant**
to the bombs next to schools and temples,
the swastikas carved
in museum stones,
the fear that whispers
*"hide,"*
the anxiety that asks
*"am I safe to be myself here?"*
the certainty that says
*"never fully."*
the confusion that wonders
*"why is that?"*
the voice that whispers back
*"because you're Jewish."*

**And when someone comes up and asks,**
*"You have a Jewish nose — are you Jewish?"*
I think to myself:
is that a question,
or an accusation?

**My skin doesn't shield**
generations of trauma,
doesn't erase stories
my family never fully tells—
but I *carry* them
in my bones,
in my breath,
in the silence
when someone asks,

*"Are Jews white?"*

**Because the truth**
is deeper
than skin,
more complicated
than color,
more real
than convenient labels
that fade
when the hate becomes
inconvenient
to explain.

**I am Jewish.**
A testament to my family's resilience,
woven from Morocco
to Ukraine
to Philadelphia
to LA.
My whiteness
never fully protected us,
and never defined
who we are.

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
    animation-duration: 0.95s; /* Slightly slower animation */
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

def create_letter_animation_html(html_text, delay_increment=0.04):
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
