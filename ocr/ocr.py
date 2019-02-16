from google.cloud import vision

client = vision.ImageAnnotatorClient.from_service_account_file('credentials/uncommonhacks-memesearch-7a7faabf16ff.json')
response = client.annotate_image({
  'image': {'source': {'image_uri': 'https://afinde-production.s3.amazonaws.com/uploads/card_1dd616ad-f0d0-45d3-8909-24b578014654.jpg'}},
  'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],
})

print(response)
