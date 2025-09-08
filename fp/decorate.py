from collections.abc import Callable

def replacer(old, new):
    def replace(decorated_func: Callable[[str], str]):
#        nonlocal old, new
        def wrapper(text: str):
#            nonlocal old, new
            text = text.replace(old, new)
            return decorated_func(text)
        return wrapper
    return replace


@replacer('&', "&amp;")
@replacer('<', "&lt;")
@replacer('>', "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"

print(tag_pre('<a href="https://blog.boot.dev/wiki/troubleshoot-code-editor-issues/">link</a>'))
