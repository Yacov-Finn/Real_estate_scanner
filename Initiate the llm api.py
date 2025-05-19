# To install or upgrade the cohere package, run this command in your terminal:
# python -m pip install cohere --upgrade


import cohere

co = cohere.ClientV2("muBD3GeIzu07TiW6i6f2Q1ygilrKdITg6WfHRlFw")
response = co.chat(
    model="command-a-03-2025", 
    messages=[{"role": "user", "content": "what are the first 5 prime numbers?"}],
    
)

print(response.message.content[0].text)

