import copy

def css_styles(initial_styles: dict[str, dict[str, str]]):
    copy_of_initial_styles = copy.deepcopy(initial_styles)
    def add_style(selector: str, property: str, value: str):
        nonlocal copy_of_initial_styles
        if selector in copy_of_initial_styles:
            copy_of_initial_styles[selector][property] = value
            return copy_of_initial_styles
        copy_of_initial_styles.update({selector: {property: value}})
        return copy_of_initial_styles
    return add_style

initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}


add_style = css_styles(initial_styles)

print(add_style("p", "color", "gray"))
