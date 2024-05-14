#ii) Convert emoji into text in Python - Converting emoticons or emojis into text in Python can be done using thedemoji module. It is used to accurately remove and replace emojis in text strings

import demoji

def convert_emojis_to_text(input_text):

    try:


        cleaned_text = demoji.replace(input_text)
        return cleaned_text
    except Exception as e:
        return f"Error: {str(e)}"

input_text_with_emojis = "I love Python! 😍🐍"
converted_text = convert_emojis_to_text(input_text_with_emojis)
print(f"Converted text: {converted_text}")
