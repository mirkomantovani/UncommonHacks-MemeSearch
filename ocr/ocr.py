from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_file('/Users/jayu/Documents/dev/uncommonhacks2019/credentials/uncommonhacks-memesearch-7a7faabf16ff.json')

def process_image_urls(urls):
    results = []
    for counter, url in enumerate(urls):
        request = {'image': {'source': {'image_uri': url}},
                        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
                        'image_context': {"language_hints": ['en']}}
        response = client.annotate_image(request)
        results.append({'id': counter,
                        'url': url,
                        'text': response.full_text_annotation.text})
    return results

process_image_urls(['https://afinde-production.s3.amazonaws.com/uploads/card_1dd616ad-f0d0-45d3-8909-24b578014654.jpg', 'https://i.redd.it/h4rntqluid911.jpg'])

