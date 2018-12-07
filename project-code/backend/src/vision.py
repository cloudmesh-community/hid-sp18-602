import json
from googleapiclient import discovery

API_KEY='AIzaSyDASvlgiXOKlf9Spr183d-ITKkWi844nII'
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


class VisionApi(object):
    def __init__(self):
        self.vision = self._create_client()


    def _create_client(self):
        return discovery.build(
            'vision', 'v1', developerKey=API_KEY,
            discoveryServiceUrl=DISCOVERY_URL)



    def detect_labels(self, images,max_results=1,num_retries=3):
        """Uses the Vision API to annotate  image  """
        request = self.vision.images().annotate(
        body={'requests': [{
                             'image': {
                                'source':{
                                    'imageUri':images
                                     }
               		 },
                	'features': [{
                    		 'type': 'LABEL_DETECTION',
                   		 'maxResults': max_results,
               		 }]
        	    }]
        	})
        response = request.execute(num_retries=num_retries)
	label=response['responses'][0]['labelAnnotations'][0]['description']

        return label
