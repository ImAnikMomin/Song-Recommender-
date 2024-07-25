import openai
from config import OPENAI_API_KEY

class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def generate_recommendations(self, tracks):
        track_descriptions = [f"{track['track']['name']} by {track['track']['artists'][0]['name']}" for track in tracks]
        prompt = f"Recommend 5-10 similar songs to the following list and provide good explanations for why each song is a good recommendation:\n{', '.join(track_descriptions)}"

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )


        raw_output = response['choices'][0]['message']['content'].strip()


        recommendations = raw_output.split('\n')


        return [(rec, "") for rec in recommendations]
