def openai_api_call(prompt_text):
    import openai
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()

    api_key = getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set in the environment variables.")
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt_text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"
