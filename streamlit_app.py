import streamlit as st

# Set page config
st.set_page_config(page_title="Conveniently White", layout="centered")

# Custom CSS for fade-in animation
st.markdown("""
<style>
@keyframes fadeInFromShadow {
    0% {opacity: 0; text-shadow: 0px 0px 12px rgba(0,0,0,0.9);}
    100% { opacity: 1; text-shadow: none; }
}

.fade-in {
    animation: fadeInFromShadow 2.5s ease-in-out forwards;
    opacity: 0;
}

@keyframes fadeInFromShadow {
    to { opacity: 1; text-shadow: none; }
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Conveniently White")
st.write("_An Interactive Slam Poem_\n\nClick **Reveal Next Stanza** to journey through the layers of my story.")

# Full poem stanzas
stanzas = [
    "**They ask me,**  \n“Are Jews white?”  \nand I pause.  \nA single breath  \nholds centuries  \nof contradiction.",
    "**See, my skin is fair,**  \nbut the history beneath runs deep  \nin colors you can’t quite see,  \na silent tapestry of trauma  \nwoven through generations.",
    "**Imagine me, seven, in LA,**  \nminding my own business,  \nkippah balanced on my head  \nlike a crown  \nunashamed,  \nunaware  \nof the cost  \nof visibility.",
    "**Until words slice the air—**  \nslurs hurled  \nlike rocks,  \nsharp enough  \nto carve doubt  \ninto a child’s courage.",
    "**My father knew this pain**  \non Philadelphia streets,  \nswastikas scratched into his car,  \nhis body bruised by fists,  \nscars carried quietly,  \na trauma so deep  \nit only speaks in whispers —  \nor not at all.",
    "**His grandparents fled Ukraine**  \nto escape the shadow  \nof pogroms,  \nanti-Jewish violence,  \nhate-filled riots,  \nstories silenced  \nby pain too raw  \nto speak aloud,  \nghosts whisper  \nin half-forgotten Yiddish sighs.",
    "**My mother’s family lived in Morocco for centuries,**  \nskin much darker than mine,  \ngenerations born into languages older than borders,  \nuntil Nazis reached Casablanca streets,  \nsigns posted on synagogues asking for names  \nand numbers,  \nlisting Jews like livestock.",
    "**They fled poverty,**  \nfear, and hunger,  \ncrossed oceans to Oklahoma,  \nwhere children pawed my grandmother’s curls  \nliterally searching for horns,  \nhooves,  \ntails —  \nfor devils their parents swore  \nJews must be.",
    "**I have her voice recorded,**  \ntelling me softly,  \nhow strange it felt  \nto have her humanity questioned  \nby curious fingers,  \ninnocent and cruel  \nin ignorance.",
    "**Yet, they say we’re white —**  \nconveniently white,  \nwhen hate needs justification,  \nwhen trauma needs erasure,  \nwhen history needs rewriting,  \nas if skin alone defines our story,  \nas if violence checks melanin  \nbefore it strikes.",
    "**I grew up in LA,**  \nwent to school behind bulletproof glass doors,  \nbecame friends with security guards,  \nlearned safety drills  \nas easily as prayers,  \nstood quietly  \nas bomb squads detonated  \nthe threats that waited  \non bus-stop benches right outside my classroom.",
    "**I remember that one time**  \nI hurriedly locked a bathroom stall,  \nfeet tucked onto porcelain  \nto hide blinking Skechers  \nfrom some angry man,  \nbanging on doors trying to get in.  \nI heard he had a knife.",
    "**So, at seven I learned,**  \nI learned what survival means —  \na silent breath,  \nan invisible heartbeat  \n\n*SHHHHH!*",
    "**Trips to coffee shops ended**  \nwith strangers spitting  \nlectures about _“The Jews”_  \nat children who dared to exist  \nwho dared to wear their faith visibly,  \nso I learned  \nto tuck mine away,  \nonly safe within walls  \nthat became increasingly thin.",
    "**We went on a field trip**  \nto the Museum of Tolerance  \nand counted swastikas carved  \non walls.  \nWe listened to survivors speak,  \nheard their warnings—  \nvoices trembling,  \nurging us  \nto remember  \nwhat the world would rather forget.",
    "**And we did remember,**  \nbut the world has amnesia.",
    "**Because today,**  \nI see Jew-hatred  \nin Los Angeles,  \naround the world,  \nhate exploding openly  \nin the streets we once believed were safe.  \n_“Activism,”_ they call it—  \nYes, sometimes it is,  \nbut sometimes it's a mask,  \nbecause I recognize the whispers  \nof ancestors  \ncrying out from Ukrainian mass-graves,  \nfrom Moroccan cemeteries,  \nfrom Philadelphia backroads.",
    "**They ask again,**  \n“Are Jews white?”",
    "**Yes. No. Both. Neither.**  \nMy whiteness  \nis conditional,  \na temporary badge  \nstripped away  \nwhen convenient  \nto hate me openly.",
    "**My whiteness is irrelevant**  \nto the bombs next to schools and temples,  \nthe swastikas carved  \nin museum stones,  \nthe fear that whispers  \n_“hide,”_  \nthe anxiety that asks  \n_“am I safe to be myself here?”_  \nthe certainty that says  \n_“never fully.”_  \nthe confusion that wonders  \n_“why is that?”_  \nthe voice that whispers back  \n_“because you’re Jewish”_",
    "**And when someone comes up and asks,**  \n_“You have a Jewish nose — are you Jewish?”_  \nI think to myself:  \nis that a question,  \nor an accusation?",
    "**My skin doesn’t shield**  \ngenerations of trauma,  \ndoesn’t erase stories  \nmy family never fully tells—  \nbut I _carry_ them  \nin my bones,  \nin my breath,  \nin the silence  \nwhen someone asks,  \n\n_“Are Jews white?”_",
    "**Because the truth**  \nis deeper  \nthan skin,  \nmore complicated  \nthan color,  \nmore real  \nthan convenient labels  \nthat fade  \nwhen the hate becomes  \ninconvenient  \nto explain.",
    "**I am Jewish.**  \nA testament to my family’s resilience,  \nwoven from Morocco  \nto Ukraine  \nto Philadelphia  \nto LA.  \nMy whiteness  \nnever fully protected us,  \nand never defined  \nwho we are.",
    "**So ask me again —**  \n_“Are Jews white?”_  \nI’ll tell you:  \n**it’s more complicated  \nthan that.**"
]

# Track current stanza index
if "stanza_index" not in st.session_state:
    st.session_state.stanza_index = 0

# Title and instructions
st.divider()
st.markdown("# Conveniently White")
st.markdown("_An Interactive Slam Poem_")

# Display stanzas up to the current index with fade-in effect
for stanza in stanzas[:st.session_state.stanza_index]:
    st.markdown(f'<div class="fade-in">{stanza.strip()}</div><br>', unsafe_allow_html=True)

# Reveal Next Stanza button
if st.session_state.stanza_index < len(stanzas):
    if st.button("Reveal Next Stanza"):
        st.session_state.stanza_index += 1
        st.rerun()
else:
    st.write("You've reached the end of the poem. Thank you for journeying with me!")
