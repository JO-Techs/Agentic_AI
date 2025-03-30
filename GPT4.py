import openai

def analyze_code(diff):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Review this code:\n{diff}"}]
    )
    return response['choices'][0]['message']['content']
