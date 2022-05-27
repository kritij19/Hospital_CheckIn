import sys
import time
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition
from global_variables import PERSON_GROUP_ID, KEY, ENDPOINT

# Create an authenticated face client
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

def create_pgp(userId, path_to_image):
    '''Creates a person group person, detects and adds to face to it. Returns the personId or "Failed 

        Args:
            userId: A string. Will be used to initialize the person group person.
            path_to_image: Path to image containing face of individual

        Returns:
            A string containing personId if successful. "Failed" otherwise.
    '''

    # Create new person inside defined person group
    try:
        fiend = face_client.person_group_person.create(PERSON_GROUP_ID, userId) 
    except:
        return "Failed" 
    personId = fiend.person_id

    print(f"The assigned personId is {personId}")

    # Add a face to the person
    w = open(path_to_image, 'r+b') 
    try:
        res = face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, fiend.person_id, w, detection_model="detection_01")
    except Exception as e: # API exception error
        print(e)
        return "Failed"
    
    print(res)


    # Train person group
    face_client.person_group.train(PERSON_GROUP_ID)

    while (True):
        training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        if (training_status.status is TrainingStatusType.succeeded):
            break
        elif (training_status.status is TrainingStatusType.failed):
            face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
            personId = "Failed"
            sys.exit('Training the person group has failed.')
        time.sleep(5)
    
    return personId