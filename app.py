# import streamlit as st
# from search_engine import search_course

# st.set_page_config(page_title="Analytics Vidhya Smart Search", layout="wide")

# st.title("🔍 Analytics Vidhya Smart Search")
# st.write("Find the most relevant free courses easily!")

# query = st.text_input("Enter keywords (e.g., Machine Learning, NLP, Python)...")

# if query:
#     results = search_course(query, top_n=10)
#     st.subheader("📌 Recommended Courses")
    
#     for res in results:
#         st.markdown(f"### [{res['title']}]({res['url']})")
#         st.write(f"**Category:** {res['categories']}")
#         st.write("---")


import streamlit as st
from search_engine import search_course  # Function to fetch course data

# Set Streamlit Page Configuration
st.set_page_config(page_title="Analytics Vidhya Smart Search", layout="wide")

# Title and Description
st.title("🔍 Analytics Vidhya Smart Search")
st.write("Find the most relevant free courses easily!")

# Input for Search Query
query = st.text_input("Enter keywords (e.g., Machine Learning, NLP, Python)...")

# Initialize session state for saved courses
if "saved_courses" not in st.session_state:
    st.session_state.saved_courses = []

# Search and Display Results
if query:
    with st.spinner("🔄 Searching for courses... Please wait."):
        results = search_course(query, top_n=10)

    if results:
        st.subheader("📌 Recommended Courses")

        for res in results:
            with st.expander(f"📖 {res['title']}"):
                st.markdown(f"### [{res['title']}]({res['url']})")

                # Display Course Image (if available)
                if "image_url" in res:
                    st.image(res["image_url"], width=300)

                # Save Button
                if st.button("❤️ Save Course", key="save_" + res["url"]):
                    if res not in st.session_state.saved_courses:
                        st.session_state.saved_courses.append(res)
                        st.success("Course saved!")

                st.write("---")

    else:
        st.warning("No courses found. Try different keywords.")

# Show Saved Courses
if st.session_state.saved_courses:
    st.subheader("💾 Saved Courses")
    
   
    saved_courses_copy = st.session_state.saved_courses.copy()
    
    for res in saved_courses_copy:
        st.markdown(f"### [{res['title']}]({res['url']})")

        # Remove Button
        if st.button("🗑 Remove", key="remove_" + res["url"]):
            st.session_state.saved_courses.remove(res)
            st.rerun()  
        
        st.write("---")
