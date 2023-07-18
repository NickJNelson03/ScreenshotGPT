import pytesseract
from PIL import Image
import openai

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'  # Replace with your actual API key

# Extract text from the image
image_path = '/path/to/your/image.png' # Replace image with the name of your photo
extracted_text = extract_text_from_image(image_path)

# Generate a response from ChatGPT
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Give key points and critical information."}, # What would you like it to do for you
        {"role": "user", "content": extracted_text} # Extracting the text as a huge chunk(large strings) or one big text(one large string)
    ]
)

# Extract the assistant's reply
assistant_reply = response['choices'][0]['message']['content']

# Print the assistant's reply
print(assistant_reply)
