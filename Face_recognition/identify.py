import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
# from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition
from global_variables import PERSON_GROUP_ID, KEY, ENDPOINT, PERSON_GROUP_NAME
import mysql.connector
from mysql.connector import Error

# Create an authenticated face client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def identify(image_path):
    """"Identify people present in picture specified by image path and return person Id if identification successful

        Args:
            image_path: a path to image containing faces to be recognized
        
        Returns:
            A string containing person Id if face recognized. An empty string otherwise.
    """

    # Open image for face recognition
    image = open(image_path, 'r+b')


    # Detect all faces in the picture
    try:
        faces = face_client.face.detect_with_stream(image, 
                                                detection_model='detection_03',
                                                recognition_model='recognition_03', 
                                                return_face_attributes=['qualityForRecognition'])
    except Exception as e: # API Exception Error
        print(f"Exception occured: {e}")   
        return []                                         

    # Get face ids for faces detected
    face_ids = []
    for face in faces:
        face_ids.append(face.face_id)

    # Identify detected faces
    try:
        results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
    except Exception as e:
        print(f"Exception occured: {e}")  
        return []

    print('Identifying faces in {}'.format(os.path.basename(image.name)))

    # If no person recognized from picture
    if not results:
        print('No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))

    # For all faces identified  
    for person in results:
        if len(person.candidates) > 0: # if detected face has atleast 1 possible candidate
            print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score              
            person_id  = person.candidates[0].person_id # get person ID for detected face
            print(person_id)
            return person_id
