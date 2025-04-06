import requests

url = 'https://res.cloudinary.com/jerrick/image/upload/v1707401113/65c4df99f485f6001d076160.jpg'

response = requests.get(url)

# with open('spring.jpg', mode='wb') as file:
#     content = response.content
#     content += b'23213213123 Kolya'
#     file.write(content)

with open('spring.jpg', mode='rb') as file:
    print(file.read())
pass
