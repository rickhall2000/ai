import openai
import os

# Initialize the OpenAI client with your API key
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def get_image_response(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


if __name__ == "__main__":
    user_input = input("What would you like to see?: ")
    gpt_response = get_image_response(user_input)
    print(f"GPT-3 Says: {gpt_response}")
