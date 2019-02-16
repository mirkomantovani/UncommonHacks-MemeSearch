from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/jayu/Documents/dev/uncommonhacks2019/credentials/uncommonhacks-memesearch-7a7faabf16ff.json')

def process_image_urls(urls):
    requests = []
    for url in urls:
        requests.append({'image': {'source': {'image_uri': url}},
                        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
                        'image_context': {"language_hints": ['en']}})
    responses = client.batch_annotate_images(requests)
    print(responses)

process_image_urls(['https://afinde-production.s3.amazonaws.com/uploads/card_1dd616ad-f0d0-45d3-8909-24b578014654.jpg', 'https://i.redd.it/h4rntqluid911.jpg'])

