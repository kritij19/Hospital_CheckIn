from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from global_variables import PERSON_GROUP_ID, KEY, ENDPOINT, PERSON_GROUP_NAME

# Create an authenticated FaceClient
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Create a PersonGroup reference class
try:  
    face_client.person_group.create(person_group_id = PERSON_GROUP_ID, name = PERSON_GROUP_NAME, recognition_model = "recognition_03")
    print('person group with ID: {0} and name: {1} created.'.format(PERSON_GROUP_ID, PERSON_GROUP_NAME))
    
# In case of APIErrorException
except: 
    print('person group {0}:{1} already exist.'.format(PERSON_GROUP_ID, PERSON_GROUP_NAME)) 