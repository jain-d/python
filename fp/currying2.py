# FORMAT    ==> create_markdown_image(alt_text)(img_url)(title) <==

def create_markdown_image(alt_text):
    final_url = f"![{alt_text}]"
    def add_url(img_url):
        nonlocal final_url
        final_url = f"{final_url}({(img_url.replace("(", "%28")).replace(")", "%29")})"
        def add_title(title=None):
            nonlocal final_url
            if title:
                final_url = f"{final_url.replace(")", "")} \"{title}\")"
            return final_url
        return add_title
    return add_url


alt_text_image = create_markdown_image("Link to google")
image_url = alt_text_image("https://google(fake).com")
tooltip_title = image_url()

print(tooltip_title)
