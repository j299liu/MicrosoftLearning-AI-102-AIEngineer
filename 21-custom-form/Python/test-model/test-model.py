import os 
from dotenv import load_dotenv

from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        form_endpoint = os.getenv('FORM_ENDPOINT')
        form_key = os.getenv('FORM_KEY')
        
        # Create client using endpoint and key
        form_recognizer_client = FormRecognizerClient(form_endpoint, AzureKeyCredential(form_key))
        form_training_client = FormTrainingClient(form_endpoint, AzureKeyCredential(form_key))

        # Model ID from when you trained your model.
        model_id = os.getenv('MODEL_ID')

        # Test trained model with a new form 
        with open('test1.jpg', "rb") as f: 
            poller = form_recognizer_client.begin_recognize_custom_forms(
                model_id=model_id, form=f)

        result = poller.result()

        for recognized_form in result:
            print("Form type: {}".format(recognized_form.form_type))
            for name, field in recognized_form.fields.items():
                print("Field '{}' has label '{}' with value '{}' and a confidence score of {}".format(
                    name,
                    field.label_data.text if field.label_data else name,
                    field.value,
                    field.confidence
                ))

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()


# OUTPUT of test1.jpg
# Form type: form-4976dff2-4e55-4aa9-835d-4bbd75f3f379
# Field 'Quantity' has label 'Quantity' with value 'None' and a confidence score of 1.0
# Field 'Signature' has label 'Signature' with value 'Josh Granger' and a confidence score of 1.0
# Field 'CompanyPhoneNumber' has label 'CompanyPhoneNumber' with value '234-986-6454' and a confidence score of 1.0
# Field 'DatedAs' has label 'DatedAs' with value '04/04/2020' and a confidence score of 1.0
# Field 'PurchaseOrderNumber' has label 'PurchaseOrderNumber' with value '3929423' and a confidence score of 1.0
# Field 'CompanyName' has label 'CompanyName' with value 'Yoga for You' and a confidence score of 1.0
# Field 'Tax' has label 'Tax' with value '$600.00' and a confidence score of 1.0
# Field 'Website' has label 'Website' with value 'www.herolimited.com' and a confidence score of 1.0
# Field 'PhoneNumber' has label 'PhoneNumber' with value '555-348-6512' and a confidence score of 1.0
# Field 'Email' has label 'Email' with value 'accounts@herolimited.com' and a confidence score of 1.0
# Field 'Total' has label 'Total' with value '$7350.00' and a confidence score of 1.0
# Field 'CompanyAddress' has label 'CompanyAddress' with value '343 E Winter Road Seattle, WA 93849 Phone:' and a confidence score of 1.0
# Field 'Subtotal' has label 'Subtotal' with value '$6750.00' and a confidence score of 1.0
# Field 'VendorName' has label 'VendorName' with value 'Seth Stanley' and a confidence score of 1.0
# Field 'Merchant' has label 'Merchant' with value 'Hero Limited' and a confidence score of 1.0