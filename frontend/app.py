import os
import sys
import streamlit as st

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from backend.rag.pipeline import RAGPipeline

UI_CONFIG = {
    "app_name": "AgriAssist-MY",
    "tagline": "Your Smart Agriculture Scheme Assistant",
    "subtitle": "AI-powered guidance for DOA Malaysia schemes, certifications and farmer services.",
    "menu": [
        "Home",
        "Ask AgriAssist",
        "Certification Schemes",
        "Farmer Services",
        "DOA Information",
        "Source Explorer",
        "Contact DOA",
    ],
    "quick_questions": [
        "What is myGAP?",
        "What is myOrganic?",
        "What is myGAP Pesticide Free?",
        "What certification schemes are available?",
        "What is the objective and function of the Department of Agriculture?",
        "How do I apply for certification?",
    ],
}

st.set_page_config(
    page_title=UI_CONFIG["app_name"],
    page_icon="🌾",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #ecfdf3, #f8fff9);
}
.block-container {
    padding-top: 1.2rem;
}
.hero {
    background: linear-gradient(rgba(10,80,35,.82), rgba(10,80,35,.82)),
                url("https://images.unsplash.com/photo-1500382017468-9049fed747ef");
    background-size: cover;
    background-position: center;
    color: white;
    padding: 42px;
    border-radius: 26px;
    box-shadow: 0 14px 35px rgba(0,0,0,.18);
}
.hero h1 {
    font-size: 46px;
    margin-bottom: 4px;
}
.card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #d8eadf;
    box-shadow: 0 8px 24px rgba(0,0,0,.07);
}
.green-card {
    background: linear-gradient(135deg, #14532d, #15803d);
    color: white;
    padding: 20px;
    border-radius: 20px;
    min-height: 135px;
    box-shadow: 0 10px 28px rgba(20,83,45,.25);
}
.answer-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border-left: 6px solid #16a34a;
    box-shadow: 0 10px 25px rgba(0,0,0,.08);
    line-height: 1.7;
}
.menu-note {
    background: #e8f7ee;
    padding: 10px;
    border-radius: 12px;
    color: #14532d;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "history" not in st.session_state:
    st.session_state.history = []

if "language" not in st.session_state:
    st.session_state.language = "English"

with st.sidebar:
    st.markdown("## 🌾 AgriAssist-MY")
    st.caption("DOA Malaysia RAG Assistant")
    st.divider()

    for item in UI_CONFIG["menu"]:
        if st.button(item, use_container_width=True):
            st.session_state.page = item

    st.divider()
    st.markdown(
        f"<div class='menu-note'>Current Page: {st.session_state.page}</div>",
        unsafe_allow_html=True,
    )

top_left, top_right = st.columns([3, 1])

with top_left:
    st.markdown(f"""
    <div class="hero">
        <h1>{UI_CONFIG["app_name"]}</h1>
        <h3>{UI_CONFIG["tagline"]}</h3>
        <p>{UI_CONFIG["subtitle"]}</p>
    </div>
    """, unsafe_allow_html=True)

with top_right:
    st.session_state.language = st.selectbox(
        "Translate answer to",
        ["English", "Malay", "Chinese", "Tamil"],
        index=["English", "Malay", "Chinese", "Tamil"].index(st.session_state.language),
    )

st.write("")

page = st.session_state.page

if page == "Home":
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("<div class='green-card'><h4>Government Schemes</h4><p>Find DOA schemes and services.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='green-card'><h4>Certification Help</h4><p>myGAP, myOrganic, myGAP.PF.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='green-card'><h4>Farmer Guidance</h4><p>Simple AI answers from DOA content.</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='green-card'><h4>Source Grounded</h4><p>Answers from your FAISS knowledge base.</p></div>", unsafe_allow_html=True)

    st.info("Go to **Ask AgriAssist** from the sidebar to ask questions.")

elif page == "Ask AgriAssist":
    left, right = st.columns([2.2, 1])

    with left:
        st.markdown("<div class='card'><h3>Ask AgriAssist</h3><p>Ask about DOA schemes, certification, eligibility, objectives or application process.</p></div>", unsafe_allow_html=True)

        query = st.text_input("Question", placeholder="Example: What is myGAP?")
        search_clicked = st.button("Search", type="primary")

        st.markdown("### Quick Questions")
        qcols = st.columns(3)

        for i, question in enumerate(UI_CONFIG["quick_questions"]):
            with qcols[i % 3]:
                if st.button(question, use_container_width=True):
                    query = question
                    search_clicked = True

        if search_clicked and query:
            final_query = f"""
            Answer the user in {st.session_state.language}.
            Use the DOA Malaysia knowledge base only.
            User question: {query}
            """

            with st.spinner("Searching DOA knowledge base..."):
                rag = RAGPipeline()
                answer = rag.ask(final_query)

            st.session_state.history.append(query)

            st.markdown("### Answer")
            st.markdown(f"<div class='answer-card'>{answer}</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='card'><h4>Conversation History</h4></div>", unsafe_allow_html=True)
        if st.session_state.history:
            for h in st.session_state.history[-5:]:
                st.write("•", h)
        else:
            st.caption("No searches yet.")

elif page == "Certification Schemes":
    st.markdown("## Certification Schemes")
    st.markdown("""
    <div class="card">
    <ul>
        <li>myGAP</li>
        <li>myOrganic</li>
        <li>myGAP Pesticide Free</li>
        <li>Phytosanitary Certification</li>
        <li>Planting Material Verification</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Farmer Services":
    st.markdown("## Farmer Services")
    st.markdown("<div class='card'><p>Search DOA advisory services, laboratory services, soil services, training and agricultural support pages.</p></div>", unsafe_allow_html=True)

elif page == "DOA Information":
    st.markdown("## DOA Information")
    st.markdown("<div class='card'><p>This assistant uses official Department of Agriculture Malaysia webpage content scraped into your local RAG knowledge base.</p></div>", unsafe_allow_html=True)

elif page == "Source Explorer":
    st.markdown("## Source Explorer")
    st.markdown("<div class='card'><p>Source files are stored in <b>data/raw_html/pages</b> and indexed into FAISS.</p></div>", unsafe_allow_html=True)

elif page == "Contact DOA":
    st.markdown("## Contact DOA")
    st.markdown("<div class='card'><p>For official enquiries, please refer to the Department of Agriculture Malaysia contact page.</p></div>", unsafe_allow_html=True)