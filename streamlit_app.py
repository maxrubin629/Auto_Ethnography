import streamlit as st
import re
import textwrap

st.set_page_config(page_title="Conveniently White", layout="centered")

# My beautiful poem that doesn't like to work for some reason
poem = textwrap.dedent("""**They ask me,**
"Are Jews white?"
and I pause.
A single breath
holds centuries
of contradiction.

**See, my skin is fair,**
but the history beneath runs deep
in colors you can't quite see,
a silent portrait of trauma
painted over generations.

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
into a child's mind.

**My father knew this pain too**
in Philadelphia backstreets,
swastikas scratched into his car,
his body bruised by fists,
scars carried quietly,
a trauma so deep
it only speaks in whispers —
or not at all.

**His family fled Ukraine**
to escape the shadow
of pogroms,
anti-Jewish violence,
hate-filled riots,
stories _silenced_
by pain too raw
to speak aloud,
ghosts whisper
in half-forgotten Yiddish sighs.

**My mother's family lived in Morocco for centuries,**
skin much darker than mine,
generations born into languages older than borders,
until Nazis reached Casablanca,
posting signs on synagogues,
asking for names,
house numbers,
listing Jews like livestock.

**They fled danger, poverty,**
fear, and hunger,
crossed oceans to Oklahoma,
where cute little children pawed my grandmother's curls
but they were looking for something — 
horns,
hooves,
tails —
for devils they were taught
Jews must be.

**As I recall it,**
I hear her voice,
telling me softly,
how strange it felt
to have her humanity questioned
by curious little fingers,
innocent and cruel
in ignorance.

**Yet, they say we're white —**
_conveniently_ white.
When hate needs justification,
when trauma needs erasure,
when history needs rewriting,
as if skin alone defines our story,
as if violence checks melanin
before it strikes.

**I grew up in LA,**
went to school behind bulletproof glass,
became friends with security guards,
learned safety drills
as easily as prayers,
sat quietly
as bomb squads detonated
the threats that waited
on bus-stop benches right outside my classroom.

**I remember that one time**
I hurriedly locked a bathroom stall,
feet tucked onto porcelain
to hide blinking Skechers
from some angry man,
carrying on about *"The Jews"*,
banging on doors trying to find me.
I later learned he had a knife.

**So, at six I learned,**
I learned what survival means —
a silent breath,
an invisible heartbeat

***SHHHHH!***

**I still didn't get it**
Trips to coffee shops ended
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

**And when someone randomly comes up and asks,**
*"You have a Jewish nose — are you Jewish?"*
I think to myself:
is that a question,
or an _accusation?_

**You see, my skin doesn't shield**
generations of trauma,
doesn't erase stories
my family never fully tells —
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
Our 'whiteness'
never fully protected us,
and never defined
who we are.

**So ask me again —**
*"Are Jews white?"*
I'll tell you:
**it's more complicated
than that.**
""")

# Custom CSS for letter fade-in animation. Thanks chatty lol!
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
    
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
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
            
            result.append(char)
        else:
            
            if char.strip(): 
                span = f'<span class="letter-fade" style="animation-delay:{delay:.3f}s">{char}</span>'
                result.append(span)
                delay += delay_increment
            else:
               
                result.append(char)
    
    return ''.join(result)


st.title("Conveniently White")
st.write("by Max Rubin")
st.write("_An 'Interactive' Slam Poem_\n\nClick **Reveal my Story** to see it gently emerge letter by letter from shadows.")

if "show_poem" not in st.session_state:
    st.session_state.show_poem = False

# button to show poem
if st.button("Reveal my Story"):
    st.session_state.show_poem = True

# Pretty animation for the reveal
if st.session_state.show_poem:
    # Process the poem text
    html_poem = convert_markdown_to_html(poem)
    animated_poem = create_letter_animation_html(html_poem)
    
    # put in a container
    st.markdown(
        f'<div class="poem-container">{animated_poem}</div>',
        unsafe_allow_html=True
    )
    
    # End poem
    st.write("\nYou've reached the end of the poem. Thank you for going on this journey with me!")
