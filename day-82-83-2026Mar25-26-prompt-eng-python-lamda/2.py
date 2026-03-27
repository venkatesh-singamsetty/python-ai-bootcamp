def create_prompt():
    topic = input("Enter the topic for the story: ")
    tone = input("Enter the tone (e.g., serious, humorous, adventurous): ")
    
    prompt = f"Write a {tone} story about {topic}."
    return prompt
# Generate prompt based on user input
user_prompt = create_prompt()
print("Generated Prompt:", user_prompt)
