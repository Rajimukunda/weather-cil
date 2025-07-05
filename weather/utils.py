def format_weather(data):
    name = data['name']
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"Weather in {name}: {temp}°C, {desc.capitalize()}"
