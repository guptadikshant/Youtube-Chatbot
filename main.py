import os
import uuid

import streamlit as st
from dotenv import load_dotenv, find_dotenv

from models import get_model_output
from utils import download_youtube_video_transcript

load_dotenv(find_dotenv())


def main() -> None:
    st.set_page_config(page_title="Youtube Chatbot")
    st.title("Youtube Chatbot")

    # Initialize the video_links dictionary in session state
    if "video_links" not in st.session_state:
        st.session_state.video_links = {}
    
    if "video_file_path" not in st.session_state:
        st.session_state.video_file_path = None
    
    video_link = st.text_input("Upload your videos here.....")

    saved_videos_dir = "saved_videos_dir"
    
    if video_link:
        with st.spinner("Saving Video Transcript. This will take few mins......."):
            # Check if the video link is new or already processed
            if video_link not in st.session_state.video_links:
                # Generate a new UUID for the new video link
                new_uuid = uuid.uuid4()
                st.session_state.video_links[video_link] = new_uuid

                # Create a new subdirectory with the generated UUID
                st.session_state.video_file_path = os.path.join(saved_videos_dir, str(new_uuid))
                os.makedirs(st.session_state.video_file_path, exist_ok=True)

                download_youtube_video_transcript(
                    video_link=video_link,
                    path=os.path.abspath(st.session_state.video_file_path)
                )
                st.success("Video transcript saved successfully!!!")
            else:
                # Use the existing UUID for the video link
                st.session_state.video_file_path = os.path.join(saved_videos_dir, str(st.session_state.video_links[video_link]))
                st.write(f"Using existing directory: {st.session_state.video_file_path}")
    
    user_question = st.text_input("Enter your questions here......")

    generate_response = st.button("Generate Response")

    if user_question and generate_response:
        with st.spinner("Generating Response....."):
            with open(os.path.join(st.session_state.video_file_path, "transcript.txt"), "r") as file:
                transcript_data = file.read()

            final_output = get_model_output(
                video_transcript=transcript_data,
                question=user_question
            )

            if final_output:
                st.write(final_output)


if __name__ == '__main__':
    main()
