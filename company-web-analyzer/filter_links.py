import json
import openai
from shared.utils.Website import Website

from prompts import link_filter_system_prompt, link_filter_user_prompt


def filter_links(model, url):
    website = Website(url)
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": link_filter_system_prompt},
            {"role": "user", "content": link_filter_user_prompt(website)}
      ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result) # type: ignore