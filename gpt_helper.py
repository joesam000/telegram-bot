from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def ask_chatgpt(question, sheet_data):
    context = f"Here is the Google Sheet data:\n{sheet_data}\n\nAnswer the question using only this data. If not found, say 'Not found in sheet'."
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
