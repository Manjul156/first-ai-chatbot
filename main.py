from openai import OpenAI

client = OpenAI()


def chat_with_chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_chatbot(user_input)
        print(f"Chatbot: {response}")