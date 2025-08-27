add the prerequisites : uv venv uv add python-dotenv openai tavily-python openai-agents loguru mistralai
run the file : uv run modules/asses2/main.py
Ask about the game recommendation example : user : Can you recommend me RPG games ? (it will run game_recommendation function)
Once the bot provide you with the list, ask for detail about the game example User : Give me the details about Skyrim (it will run gamedetail_info function)
.env files content : OPENAI_API_KEY MISTRAL_API_KEY
