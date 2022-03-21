# Handler
def handler(event, context):
    return hello(event.name)

def hello(name: str) -> str:
    return f"Hello {name}!"