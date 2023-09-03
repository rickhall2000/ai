import openai
import os

# Initialize the OpenAI client with your API key
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def get_gpt_response(prompt):
    """Get a response from GPT-3 model based on the provided prompt."""
    response = openai.Completion.create(
        engine="davinci",  # Use the 'davinci' model, which is one of the most capable models
        prompt=prompt,
        max_tokens=150  # Limit the response to 150 tokens
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = input("Ask GPT-3: ")
    gpt_response = get_gpt_response(user_input)
    print(f"GPT-3 Says: {gpt_response}")
