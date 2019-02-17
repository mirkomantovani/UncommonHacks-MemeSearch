from google.cloud import vision
import pickle

image_client = vision.ImageAnnotatorClient.from_service_account_file('uncommonhacks-memesearch-7a7faabf16ff.json')

def chunks(urls):
    for i in range(0, len(urls), 16):
        yield urls[i:i+16]

def process_image_urls(urls):
    requests = []
    results = {}
    chunked_urls = chunks(urls)
    for chunk in chunked_urls:
        for url in chunk:
            request = {'image': {'source': {'image_uri': url}},
                       'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
                       'image_context': {"language_hints": ['en']}}
            requests.append(request)
        response = image_client.batch_annotate_images(requests)
        for counter, url in enumerate(chunk):
            results[url] = response.responses[counter].full_text_annotation.text
        requests.clear()
    return results

#urls = [
#            'https://i.redd.it/dfhv8xzspif21.jpg',
#            'https://i.redd.it/9834v131uyd21.jpg',
#            'https://i.redd.it/8tva97jmksf21.jpg',
#            'https://i.redd.it/5s65b1xh7gc21.jpg',
#            'https://i.redd.it/h31caipsume21.jpg',
#            'https://i.imgur.com/kesnukh.jpg',
#            'https://i.redd.it/5sjwxk03lbg21.jpg',
#            'https://i.redd.it/3cybnjz9a7b21.jpg',
#            'https://i.redd.it/h5euiwba1ff21.jpg',
#            'https://i.imgur.com/b1rmBnp.jpg']

#print(process_image_urls(urls))

