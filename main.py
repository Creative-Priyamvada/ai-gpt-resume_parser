


from pdf2text import pdf_to_text
from flask import Flask, request, jsonify
from calling_chatGPT import chatGPT_output
import os


app = Flask(__name__)

# API endpoint for converting PDF to text and processing with chatGPT
@app.route('/convert', methods=['POST'])
def convert_pdf():
    # Get the PDF file from the request
    #file = request.files['file']
    
    # Save the PDF file locally
    #file_path = "temp.pdf"
    #file.save(file_path)
    pdf_path = "resume.pdf"
    
    # Extract text from the PDF
    resume_text = pdf_to_text(pdf_path)
    
    # Process the text with chatGPT
    o=chatGPT_output(resume_text)
    
    # Remove the temporary PDF file
    #os.remove(file_path)
    
    return jsonify({'message': 'PDF converted and processed successfully', 'o': o})



# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True,port=8001)