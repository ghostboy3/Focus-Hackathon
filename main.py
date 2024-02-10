from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st

def generateTranscript(id):
    # video_id = 'fYyARMqiaag'
    video_id = id
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Extract the text from the transcript
    captions_text = ''
    for segment in transcript:
        caption = segment['text']
        captions_text += caption + ' '

    # Print the extracted text
    return captions_text

def generateResponse(question, lesson):
    prompt = "This is a university lesson: " + lesson + " answer this quesion as if you taught this lesson, Question: " + question 

st.title('My First Streamlit App')
user_input = st.text_input("Enter your video ID")
st.write('The user entered:', generateTranscript(user_input))

