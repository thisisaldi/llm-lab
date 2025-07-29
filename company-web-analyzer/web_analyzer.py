import openai
from get_website_details import get_website_details
from prompts import analyzer_system_prompt, analyzer_user_prompt

def analyze_website(model, company_name, url):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": analyzer_system_prompt},
            {"role": "user", "content": analyzer_user_prompt(model, company_name, url)}
          ],
    )
    result = response.choices[0].message.content
    return result