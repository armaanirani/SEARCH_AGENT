import streamlit as st
from agent_utils import get_search_results

st.set_page_config(
    page_title="GenAI Search Agent",
    page_icon=":robot_face:",
    layout="centered"
)

st.title("Ask GenAI Search Agent")

query = st.text_input("Enter your query:", placeholder="e.g. What are the latest updates in the world of AI?")


if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            results = get_search_results(query)
        st.success("Search results:")
        st.write(results)
    else:
        st.warning("Please enter a query.")