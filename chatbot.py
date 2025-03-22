from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Select the model from the Hugging Face model hub
model_name = "facebook/blenderbot-400M-distill"

# This will download the model and tokenizer to a directory on your local machine. 
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Let's initialize this list before any conversations occur.
conversation_history = []

while True:
    # Use the join() method in Python to concatenate the conversation history list into a single string
    history_string = "\n".join(conversation_history)

    # Fetch prompt from user
    input_text = input("> ")

    # Tokenize the input text and history string 
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    # Generate a response from the model 
    outputs = model.generate(**inputs, max_length=50)

    # Decode the generated tokens to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(response)
    print(outputs)

    # Append the input text and response to the conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    print(conversation_history)