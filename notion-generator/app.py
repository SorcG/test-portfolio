import streamlit as st
from claude_client import generate_content
from notion_wrapper import create_page
from prompts import CONTENT_TYPES

st.set_page_config(page_title="Claude → Notion Generator", page_icon="✍️", layout="centered")

st.title("Claude → Notion Generator")
st.caption("Generate structured content with Claude AI and save it directly to Notion.")

st.divider()

topic = st.text_input("Topic", placeholder="e.g. The future of renewable energy")
content_type = st.selectbox("Content type", CONTENT_TYPES)

if st.button("Generate", type="primary", disabled=not topic.strip()):
    with st.spinner("Claude is generating your content..."):
        try:
            result = generate_content(topic.strip(), content_type)
            st.session_state["generated"] = result
            st.session_state["topic"] = topic.strip()
        except Exception as e:
            st.error(f"Error generating content: {e}")

if "generated" in st.session_state:
    st.divider()
    st.subheader("Preview")
    st.markdown(st.session_state["generated"])

    st.divider()
    if st.button("Save to Notion", type="secondary"):
        with st.spinner("Creating Notion page..."):
            try:
                url = create_page(st.session_state["generated"])
                st.success("Page created successfully!")
                st.link_button("Open in Notion", url)
            except Exception as e:
                st.error(f"Error creating Notion page: {e}")
