from openai import OpenAI
key = "Paste Your OpenAi API Key"

messages = [] 

client = OpenAI(api_key=key)

def completion(messageu):
    global messages
    messages.append({
        "role":"user",
        "content":messageu
    })

    chat_completion = client.chat.completions.create(messages=messageu,model="gpt-4o")

    # Message Of AI
    message = {
        "role":"Assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(message)
    print(f"Jarvis: {message[content]}")

if __name__=="__main__":
    user_input = input("Hey, I am Jarvis, How may I Help You?\n")
    print(f"User: {user_input}")
    completion(user_input)