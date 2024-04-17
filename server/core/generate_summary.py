import os
from time import sleep
from openai import OpenAI

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")

def save_file(filepath, content):
    # Create the parent directory of the file if it does not exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

# Define the chatbot function
def chatbot(conversation, model="gpt-3.5-turbo", temperature=0, max_tokens=2500):
    max_retry = 7
    retry = 0
    while True:
        try:
            # Attempt to communicate with OpenAI
            client = OpenAI(api_key=OPEN_AI_API_KEY)            
            response = client.chat.completions.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            
            # Extract text and tokens from OpenAI response
            text = response.choices[0].message.content
            tokens = response.usage.total_tokens
                        
            return text, tokens
        except Exception as oops:
            # Handle errors by retrying
            retry += 1
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            sleep(5)
            if retry >= max_retry:
                exit()


# Define the function to use the ChatGPT API
def use_chatgpt(system_message, user_message):
    # Prepare conversation in a list format
    conversation = list()
    conversation.append({'role': 'system', 'content': system_message})
    conversation.append({'role': 'user', 'content': user_message})
    
    # Call the chatbot function to process the conversation
    text, tokens = chatbot(conversation)
    
    # Return the generated text
    return text

def generate_spr():
    # Read the prompt spr message
    system_message = open_file('core/prompt_spr.txt')

    # Path to the transcripts folders
    transcripts_folder = 'core/transcripts'

    # Get the list of transcript files
    transcript_files = [f for f in os.listdir(transcripts_folder) if f.endswith('.txt')]

    # Sort the transcript files by their last modification time
    transcript_files.sort(key=lambda x: os.path.getmtime(os.path.join(transcripts_folder, x)))

    # Process the last uploaded transcript file
    last_file = transcript_files[-1]
    transcript_path = os.path.join(transcripts_folder, last_file)

    # Read the transcript content
    user_message = open_file(transcript_path)

    # Get the response from ChatGPT
    text = use_chatgpt(system_message, user_message)

    return text
