import http.client
import json

def send_message(message):
    conn = http.client.HTTPSConnection("open-ai31.p.rapidapi.com")
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "model": "gpt-3.5-turbo"
    }
    
    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "67bbcdfa65msh06b238bcd79aa5ep1bf536jsnbbbce1615d31",
        'X-RapidAPI-Host': "open-ai31.p.rapidapi.com"
    }
    
    conn.request("POST", "/api/ai/", json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()
    
    response = json.loads(data.decode("utf-8"))
    messages = response.get("Response", None)
    
    if isinstance(messages, list):
        return messages[0].get("content", "Oops! Something went wrong.")
    else:
        return messages or "Oops! Something went wrong."

def main():
    print("Welcome to ChatGPT! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = send_message(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    main()
