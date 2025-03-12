import streamlit as st
import re

st.set_page_config(page_title="Conveniently White", layout="centered")

# Basic fade-in CSS
st.markdown("""
<style>
@keyframes fadeInFromShadow {
    0%   { opacity: 0; text-shadow: 0px 0px 12px rgba(0,0,0,0.9); }
    100% { opacity: 1; text-shadow: none; }
}
.fade-in {
    animation: fadeInFromShadow 1.5s ease-in-out forwards;
    opacity: 0;
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Conveniently White")
st.write("_An Interactive Slam Poem_\n\nClick **Reveal Next Stanza** to journey through the layers of my story.")

# Minimal "parser" for bold, italics, and line breaks
def naive_markdown_to_html(text):
    # Convert **bold** -> <b>bold</b>
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    # Convert _italics_ -> <i>italics</i>
    text = re.sub(r"_(.*?)_", r"<i>\1</i>", text)
    # Convert line breaks to <br>
    text = text.replace("\n", "<br>")
    return text

stanzas = [
     """
     **They ask me,**  
     “Are Jews white?”  
     and I pause.  
     A single breath  
     holds centuries  
     of contradiction.
     """,
     """
     **See, my skin is fair,**  
     but the history beneath runs deep  
     in colors you can’t quite see,  
     a silent tapestry of trauma  
     woven through generations.
     """,
     """
     **Imagine me, seven, in LA,**  
     minding my own business,  
     kippah balanced on my head  
     like a crown  
     unashamed,  
     unaware  
     of the cost  
     of visibility.
     """,
     """
     **Until words slice the air—**  
     slurs hurled  
     like rocks,  
     sharp enough  
     to carve doubt  
     into a child’s courage.
     """,
     """
     **My father knew this pain**  
     on Philadelphia streets,  
     swastikas scratched into his car,  
     his body bruised by fists,  
     scars carried quietly,  
     a trauma so deep  
     it only speaks in whispers —  
     or not at all.
     """,
     """
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
     """,
     """
     **My mother’s family lived in Morocco for centuries,**  
     skin much darker than mine,  
     generations born into languages older than borders,  
     until Nazis reached Casablanca streets,  
     signs posted on synagogues asking for names  
     and numbers,  
     listing Jews like livestock.
     """,
     """
     **They fled poverty,**  
     fear, and hunger,  
     crossed oceans to Oklahoma,  
     where children pawed my grandmother’s curls  
     literally searching for horns,  
     hooves,  
     tails —  
     for devils their parents swore  
     Jews must be.
     """,
     """
     **I have her voice recorded,**  
     telling me softly,  
     how strange it felt  
     to have her humanity questioned  
     by curious fingers,  
     innocent and cruel  
     in ignorance.
     """,
     """
     **Yet, they say we’re white —**  
     conveniently white,  
     when hate needs justification,  
     when trauma needs erasure,  
     when history needs rewriting,  
     as if skin alone defines our story,  
     as if violence checks melanin  
     before it strikes.
     """,
     """
     **I grew up in LA,**  
     went to school behind bulletproof glass doors,  
     became friends with security guards,  
     learned safety drills  
     as easily as prayers,  
     stood quietly  
     as bomb squads detonated  
     the threats that waited  
     on bus-stop benches right outside my classroom.
     """,
     """
     **I remember that one time**  
     I hurriedly locked a bathroom stall,  
     feet tucked onto porcelain  
     to hide blinking Skechers  
     from some angry man,
     banging on doors trying to get in.
     I heard he had a knife.
     """,
     """
     **So, at seven I learned,**
     I learned what survival means —  
     a silent breath,  
     an invisible heartbeat  
     
     *SHHHHH!*
     """,
     """
     **Trips to coffee shops ended**  
     with strangers spitting  
     lectures about _“The Jews”_  
     at children who dared to exist
     who dared to wear their faith visibly,  
     so I learned  
     to tuck mine away,  
     only safe within walls  
     that became increasingly thin.
     """,
     """
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
     """,
     """
     **And we did remember,**  
     but the world has amnesia.
     """,
     """
     **Because today,**  
     I see Jew-hatred  
     in Los Angeles,  
     around the world,  
     hate exploding openly  
     in the streets we once believed were safe.  
     _“Activism,”_ they call it—
     Yes, somtimes it is, 
     but sometimes it's a mask,
     because I recognize the whispers  
     of ancestors  
     crying out from Ukrainian mass-graves,  
     from Moroccan cemeteries,  
     from Philadelphia backroads.
     """,
     """
     **They ask again,**  
     “Are Jews white?”
     """,
     """
     **Yes. No. Both. Neither.**  
     My whiteness  
     is conditional,  
     a temporary badge  
     stripped away  
     when convenient  
     to hate me openly.
     """,
     """
     **My whiteness is irrelevant**  
     to the bombs next to schools and temples,  
     the swastikas carved  
     in museum stones,  
     the fear that whispers  
     _“hide,”_  
     the anxiety that asks  
     _“am I safe to be myself here?”_  
     the certainty that says  
     _“never fully.”_  
     the confusion that wonders  
     _“why is that?”_  
     the voice that whispers back  
     _“because you’re Jewish”_
     """,
     """
     **And when someone comes up and asks,**  
     _“You have a Jewish nose — are you Jewish?”_  
     I think to myself:  
     is that a question,  
     or an accusation?
     """,
     """
     **My skin doesn’t shield**  
     generations of trauma,  
     doesn’t erase stories  
     my family never fully tells—  
     but I _carry_ them  
     in my bones,  
     in my breath,  
     in the silence  
     when someone asks,
     
     _“Are Jews white?”_
     """,
     """
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
     """,
     """
     **I am Jewish.**  
     A testament to my family’s resilience,  
     woven from Morocco  
     to Ukraine  
     to Philadelphia  
     to LA.  
     My whiteness  
     never fully protected us,  
     and never defined  
     who we are.
     """,
     """
     **So ask me again —**  
     _“Are Jews white?”_  
     I’ll tell you:  
     **it’s more complicated  
     than that.**
     """
 ]

if "stanza_index" not in st.session_state:
    st.session_state.stanza_index = 0

# Reveal stanzas with fade-in
for i in range(st.session_state.stanza_index):
    stanza_html = naive_markdown_to_html(stanzas[i].strip())
    st.markdown(f"<div class='fade-in'>{stanza_html}</div>", unsafe_allow_html=True)

# Reveal button
if st.session_state.stanza_index < len(stanzas):
    if st.button("Reveal Next Stanza"):
        st.session_state.stanza_index += 1
        st.experimental_rerun()
else:
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
