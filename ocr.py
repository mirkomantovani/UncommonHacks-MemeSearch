from google.cloud import vision
import pickle

image_client = vision.ImageAnnotatorClient.from_service_account_file('/Users/jayu/Documents/dev/uncommonhacks2019/credentials/uncommonhacks-memesearch-7a7faabf16ff.json')

def process_image_urls(urls):
    results = []
    for counter, url in enumerate(urls):
        request = {'image': {'source': {'image_uri': url}},
                        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
                        'image_context': {"language_hints": ['en']}}
        response = image_client.annotate_image(request)
        results.append({'id': counter,
                        'url': url,
                        'text': response.full_text_annotation.text})
    return results

def pickle_results(results):
    with open('results.pickle', 'wb') as f:
        pickle.dump(results, f, pickle.HIGHEST_PROTOCOL)
