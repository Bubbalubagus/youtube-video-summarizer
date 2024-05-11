# Get Youtube MP3 file from YouTube link
# Put MP3 file through Whisper to output text
# Put whisper text into GPT-3 (davinci) w/ some Prompt Engineering and return result

import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import openai
#import whisper


def get_youtube_summary(link):
  #https://www.youtube.com/watch?v=jNQXAC9IVRw
  #https://youtu.be/4l3BzUzk9sw
  #file_name = 'song.mp3'
  #yt = YouTube(link)
  video_id = link.split('=')[-1]

  transcript = YouTubeTranscriptApi.get_transcript(video_id)

  string_list = [f"{d['text']}" for d in transcript]
  transcriptString = ' '.join(string_list)
  if transcriptString[-1] == ' ':
    transcriptString = transcriptString[:-1]

  ## Get the audio stream and download it to the current working directory
  #audio_stream = yt.streams.filter(only_audio=True).first()
  #audio_stream.download(os.getcwd())

  # Rename the file to the desired name
  #os.rename(audio_stream.default_filename, file_name)

  #model = whisper.load_model("base")
  #result = model.transcribe(file_name)
  #print(result["text"]) #uncomment this line if you want to see results of transcript
  #ytvideoText = result["text"]

  # Set the prompt
  prompt = "Summarize the main points of the following transcript into five unique bullet points, and nothing more: " + transcriptString[:2700] + "\n Summary:"  #changed from ytvideoText
  #shortenedPrompt = ' '.join(prompt.split(' ')[:2500])
  model = "text-davinci-003"

  openai.api_key = os.environ['OPENAI_API_KEY1']

  # Call the API
  completions = openai.Completion.create(model=model,
                                         prompt=prompt,
                                         max_tokens=256,
                                         temperature=0.1,
                                         top_p=1,
                                         n=1,
                                         frequency_penalty=0,
                                         presence_penalty=0)
  generated_text = completions.choices[0].text
  #new_generated_text = '\n'.join(generated_text.split("-"))
  #return new_generated_text
  return generated_text


#if __name__ == '__main__':
#  getYouTubeText('https://www.youtube.com/watch?v=jNQXAC9IVRw')
