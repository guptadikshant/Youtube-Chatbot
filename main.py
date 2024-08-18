import os
import uuid

import streamlit as st


def main() -> None:
    st.set_page_config(page_title="Youtube Chatbot")
    st.title("Youtube Chatbot")
    
    if "uuid" not in st.session_state:
        st.session_state.uuid = uuid.uuid4()

    video_link = st.text_input("Upload your videos here.....")

    generate_response = st.button("Generate Response")

    saved_videos_dir = "saved_videos_dir"

    video_file_path = os.path.join(saved_videos_dir, f"{st.session_state.uuid}")

    os.makedirs(video_file_path, exist_ok=True)

    if video_link and generate_response:
        if os.path.exists(os.path.abspath(video_file_path)):
            with open(os.path.join(video_file_path, "temp.txt"), "w") as file:
                file.write(video_link)  


if __name__ == '__main__':
    main()
