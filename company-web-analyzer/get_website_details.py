from shared.utils.Website import Website
from filter_links import filter_links

def get_website_details(model, url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    links = filter_links(model, url)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    return result