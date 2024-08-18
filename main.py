import os
import uuid

import streamlit as st

VIDEO_TRANSCRIPT = "transcript.txt"


def main() -> None:
    st.set_page_config(page_title="Youtube Chatbot")
    st.title("Youtube Chatbot")

    # Initialize the video_links dictionary in session state
    if "video_links" not in st.session_state:
        st.session_state.video_links = {}

    video_link = st.text_input("Upload your videos here.....")

    generate_response = st.button("Generate Response")

    saved_videos_dir = "saved_videos_dir"

    if video_link and generate_response:
        # Check if the video link is new or already processed
        if video_link not in st.session_state.video_links:
            # Generate a new UUID for the new video link
            new_uuid = uuid.uuid4()
            st.session_state.video_links[video_link] = new_uuid

            # Create a new subdirectory with the generated UUID
            video_file_path = os.path.join(saved_videos_dir, str(new_uuid))
            os.makedirs(video_file_path, exist_ok=True)
            st.write(f"Created directory: {video_file_path}")

        else:
            # Use the existing UUID for the video link
            video_file_path = os.path.join(saved_videos_dir, str(st.session_state.video_links[video_link]))
            st.write(f"Using existing directory: {video_file_path}")

        # Save the video link to a file in the subdirectory
        with open(os.path.join(video_file_path, VIDEO_TRANSCRIPT), "w") as file:
            file.write(video_link)


if __name__ == '__main__':
    main()
    