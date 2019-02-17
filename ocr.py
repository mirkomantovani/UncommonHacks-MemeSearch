from google.cloud import vision
import pickle

image_client = vision.ImageAnnotatorClient.from_service_account_file('uncommonhacks-memesearch-7a7faabf16ff.json')

def process_image_urls(urls):
    requests = []
    results = {}
    for url in urls:
        request = {'image': {'source': {'image_uri': url}},
                        'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
                        'image_context': {"language_hints": ['en']}}
        requests.append(request)
    response = image_client.batch_annotate_images(requests)
    for counter, url in urls:
        results[url] = response.responses[counter].full_text_annotation.text
        # results.append({'id': counter,
        #                 'url': url,
        #                 'text': response.full_text_annotation.text})
    return results

def pickle_results(results):
    with open('results.pickle', 'wb') as f:
        pickle.dump(results, f, pickle.HIGHEST_PROTOCOL)

