from flask import Flask
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from flask import render_template
from flask import request
import json

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Let's initialize this list before any conversations occur.
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_chatbot():
    try:
    
        # Reads the data from the HTTP request body. The as_text=True parameter ensures that the data is returned as a string.
        data = request.get_data(as_text=True)
        # Converts the JSON-formatted string into a Python dictionary. The json.loads() function is used for this purpose.
        data = json.loads(data)
        # Extracts the value associated with the key 'prompt' from the dictionary and assigns it to the variable input_text.
        input_text = data['prompt']

        # Create conversation history string
        history_string = "\n".join(conversation_history)

        # Tokenize the input text and history
        inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

        # Generate the response from the model
        outputs = model.generate(**inputs, max_length=50)

        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Add interaction to conversation history
        conversation_history.append(input_text)
        conversation_history.append(response)
        
        return response
        #return json.dumps({
        #    'response': response,
        #    'conversation_history': conversation_history
        #})
    except Exception as e:
        return json.dumps({'error': str(e)})   
    
# Condition ensures that the server is only run if the script is executed directly, not when imported as a module.
if __name__ == '__main__':
    #To start the server.
    app.run(debug=True)