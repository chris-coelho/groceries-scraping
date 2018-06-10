

def handle_message(e):
    if isinstance(e.args[0], list):
        return ', '.join(e.args[0])
    return ', '.join(e.args)
