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

    if "transcription_done" not in st.session_state:
        st.session_state.transcription_done = False

    # Session State Variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    with st.container():
        if not st.session_state.transcription_done:
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
                        st.session_state.transcription_done = True

    if st.session_state.transcription_done:
        # Display chat history first
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # The question-asking prompt is now placed after displaying the chat history.
        user_question = st.chat_input(placeholder="Enter your questions here......")

        if user_question:
            st.chat_message('user').markdown(user_question)
            # Save the user's input in the session and role will be user
            st.session_state.chat_history.append({"role": 'user', "content": user_question})
            with st.spinner("Generating Response....."):
                with open(os.path.join(st.session_state.video_file_path, "transcript.txt"), "r") as file:
                    transcript_data = file.read()

                with st.chat_message("assistant"):
                    final_output = get_model_output(
                        video_transcript=transcript_data,
                        question=user_question
                    )
                    if final_output:
                        # Save the AI's response and role will be of AI
                        message = {'role': 'assistant', 'content': final_output}
                        # Save its response in the session state
                        st.session_state.chat_history.append(message)
                        st.write(final_output)


if __name__ == '__main__':
    main()
