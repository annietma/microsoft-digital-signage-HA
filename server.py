# Import necessary modules
from flask import Flask, request
import os
from PIL import Image
import pytesseract

# Create a Flask app instance
app = Flask(__name__)

# Get the absolute path of the current directory
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Define a route '/upload' for handling POST requests
@app.route('/upload', methods=['POST'])
def upload():
    # Define the target directory where the uploaded images will be saved
    target = os.path.join(APP_ROOT, 'images/')
    
    # Create the target directory if it doesn't exist
    if not os.path.isdir(target):
        os.mkdir(target)
        
    # Get the 'computer_name' parameter from the request form
    computer_name = request.form.get('computer_name')
    
    # Print the received computer name to the console
    print(f'{computer_name} display received', flush=True)
    
    # Get the uploaded file from the request
    file = request.files['file']
    
    # Set the destination path for saving the uploaded image
    destination = "/".join([target, file.filename])
    
    # Save the uploaded file to the destination path
    file.save(destination)
    
    # Open the saved image using PIL (Python Imaging Library)
    img = Image.open(destination)
    
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(img)
    
    # Check if the extracted text contains the words 'correct' or 'error'
    if 'correct' not in text.lower() or 'error' in text.lower():
        # If 'correct' is not found or 'error' is present, print an error message
        print(f"{computer_name} display ERROR", flush=True)
    else:
        # If 'correct' is found and 'error' is not present, print an OK message
        print(f"{computer_name} display OK", flush=True)
    
    # Return a simple message to the client
    return 'Image saved.'

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
