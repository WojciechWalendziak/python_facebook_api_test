import facebook
import requests

# Configuration
# TODO: If you upload your app, I strongly recommend that you save your token in an environment variable.
access_token = 'EAAKfFZC2evZAgBOZC55ltxh2WhZB7smw6ZByysTfUsaMIG3b611bHZACci4agXiJqgiQ7ZBvl6cxVXej8fbPF1LZBe4WSdng0OFwriZCZBpbJHOa1RdUudgzxjg4xJ2L2ls6PIELRgombyomWMtXJSh6qwD0P6vXaZBbLD4UlvXb2ZAUrBgiKUcqh5f5VyZA7WtlLYhkZD'
api_url = 'https://cataas.com/cat'

# Connection to the Facebook API
graph = facebook.GraphAPI(access_token)

# Sending messages
def publish_cat_image(message):
    # We make a get request to the api that will return us an image of a cat
    image = requests.get(api_url).content
    graph.put_photo(message=message, image=image)

# Example of usage
publish_cat_image('New Cat !!')
