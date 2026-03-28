# Google colab

import requests
import json

# First API call with reasoning
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "openai/gpt-5.4",
    "messages": [
        {
          "role": "user",
          "content": "How many r's are in the word 'strawberry'?"
        }
      ],
    "reasoning": {"enabled": True},
    "max_tokens": 2000 # Added max_tokens
  })
)

# Extract the assistant message with reasoning_details
response_json = response.json()

if 'error' in response_json:
    print(f"API Error: {response_json['error']['message']}")
    raise SystemExit("API call failed due to error.")

response_message = response_json['choices'][0]['message']

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": response_message.get('content'),
    "reasoning_details": response_message.get('reasoning_details')  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={ # Added headers for the second API call
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "openai/gpt-5.4",
    "messages": messages,  # Includes preserved reasoning_details
    "reasoning": {"enabled": True},
    "max_tokens": 2000 # Added max_tokens
  })
)

response2_json = response2.json()
print(json.dumps(response2_json, indent=2))