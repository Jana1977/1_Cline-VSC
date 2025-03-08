#~/Documents/007_2_BIG_DATA_ARCHITECT/222_environments/AIML2025-venv/
import requests

def get_transcript(video_id, api_key):
    url = "https://www.searchapi.io/api/v1/search"
    params = {
        "engine": "youtube_transcripts",
        "video_id": video_id,
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    # Extract the transcript text
    transcript = " ".join([entry['text'] for entry in data.get('transcripts', [])])
    return transcript

def summarize_transcript(transcript, openai_api_key):
    import openai
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following transcript into bullet points:\n\n{transcript}"}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def main():
    video_id = input("Enter the YouTube video ID: ")
    searchapi_key = input("Enter your SearchAPI.io API key: ")
    openai_key = input("Enter your OpenAI API key: ")

    try:
        transcript = get_transcript(video_id, searchapi_key)
        if not transcript:
            print("No transcript found for the provided video.")
            return

        summary = summarize_transcript(transcript, openai_key)
        print("\nSummary:\n")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
