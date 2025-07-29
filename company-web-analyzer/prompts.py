from get_website_details import get_website_details


# FILTER LINKS PROMPTS

link_filter_system_prompt = """
    You are the decider who are able to decide which links that are provided is relevant about the company. 
    The links given are from a webpage that has been scraped, some may not be relevant, some are relevant.
    Your job is to filter which links are relevant. I will give an example of the answer that you must strictly follow:
    {
        "links": [
            {"type": "something page", "url": "https://example.com/to/do"},
            {"type": "about page", "url": "https://another.example.com/about"}
        ]
    }
"""

def link_filter_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
        Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt


# WEB ANALYZER PROMPTS

analyzer_system_prompt = """
    You are an assistant that helps analyze the contents of many relevant pages from a company website.
    From your analysis, create an informative summary in some form of brochure about the company for
    giving an explanation about the company that is convincing. Respond in markdown (not code blocks). Include details of company culture, customers and careers/jobs if you have
    the information.
"""

def analyzer_user_prompt(model, company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += get_website_details(model, url)
    user_prompt = user_prompt[:5_000] 
    return user_prompt