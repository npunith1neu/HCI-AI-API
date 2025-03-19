import openai

API_KEY = 'YOUR_OPEN_AI_KEY_HERE'
client = openai.OpenAI(api_key=API_KEY)

def generate_hello_world():
    """
    Generates a creative 'Hello World' message using OpenAI's GPT model.
    """
    prompt = "Generate a unique and creative 'Hello World' message with a fun twist."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens= 50,
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Fetching AI-generated Hello World message...\n")
    message = generate_hello_world()
    print(message)