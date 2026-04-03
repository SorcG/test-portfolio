import streamlit as st
from claude_client import generate_content
from notion_wrapper import create_page
from prompts import CONTENT_TYPES

st.set_page_config(page_title="Claude → Notion Generator", page_icon="✍️", layout="centered")

st.title("Claude → Notion Generator")
st.caption("Generate structured content with Claude AI and save it directly to Notion.")

st.divider()

# --- Input form ---
topic = st.text_input("Topic", placeholder="e.g. The future of renewable energy")
content_type = st.selectbox("Content type", CONTENT_TYPES)

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Tone", ["Formal", "Casual", "Professional"])
with col2:
    language = st.selectbox("Language", ["German", "English"])

# --- Generate / Regenerate buttons ---
btn_col1, btn_col2 = st.columns([3, 1])
with btn_col1:
    generate_clicked = st.button("Generate", type="primary", disabled=not topic.strip())
with btn_col2:
    regen_clicked = st.button("↺ Regenerate", disabled="generated" not in st.session_state)

if generate_clicked or regen_clicked:
    if topic.strip():
        with st.spinner("Claude is generating your content..."):
            try:
                result = generate_content(topic.strip(), content_type, tone, language)
                st.session_state["generated"] = result
                st.session_state["topic"] = topic.strip()
            except Exception as e:
                st.error(f"Error generating content: {e}")

# --- Editable preview + save ---
if "generated" in st.session_state:
    st.divider()
    st.subheader("Preview & Edit")
    edited = st.text_area(
        "You can edit the content before saving:",
        value=st.session_state["generated"],
        height=400,
        label_visibility="visible",
    )

    st.divider()
    if st.button("Save to Notion", type="secondary"):
        with st.spinner("Creating Notion page..."):
            try:
                url = create_page(edited)
                st.success("Page created successfully!")
                st.link_button("Open in Notion", url)
            except Exception as e:
                st.error(f"Error creating Notion page: {e}")
