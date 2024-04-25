def generate_image_links(base_url, start_index, end_index):
    image_links = []
    for i in range(start_index, end_index + 1):
        image_link = f'{base_url}/{i}.jpg" />'
        image_links.append(image_link)
    return image_links

base_url = '<img src="https://gi.esmplus.com/naturer112/%EB%A7%88%EC%B9%B4%EC%A0%A0'
start_index = 0
end_index = 37
image_links = generate_image_links(base_url, start_index, end_index)
for link in image_links:
    print(link)