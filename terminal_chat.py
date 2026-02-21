import requests
import uuid

API_URL = "http://127.0.0.1:8000/chat"


user_id = str(uuid.uuid4())

print("\n🎓 Study Bot Terminal Chat")
print("Type 'exit' to quit\n")

while True:
    question = input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("Bot: Goodbye 👋")
        break

    payload = {
        "user_id": user_id,
        "question": question
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            print("Bot:", response.json()["response"])
        else:
            print("Error:", response.text)

    except Exception as e:
        print("Server not running. Start uvicorn first.")
        print(e)