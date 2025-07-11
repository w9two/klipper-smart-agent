import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def send_prompt(config, logs):
    prompt = f"""
You are a 3D printer diagnostic expert. A user has provided their Klipper configuration and recent log output.
Please analyze and suggest any improvements, warnings, or fixes.

=== CONFIG START ===
{config}
=== CONFIG END ===

=== LOG START ===
{logs}
=== LOG END ===

Be concise and technical, but clear.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error contacting OpenAI: {e}"
