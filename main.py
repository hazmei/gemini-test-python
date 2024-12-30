import google.generativeai as genai
import PIL.Image
import os
import json

PROMPT = '''
Extract the recipt data and return only the name of the shop, receipt/invoice number, items purchased, each items pricing, any service and total cost. Return the result in a JSON format.
Here's an example of the result
{
  "items": [
    {
      "name": "POKKA LEMON TEA",
      "price": "0.05"
    },
  ],
  "receipt_number": "12345"
  "shop_name": "SHENG SHIONG"
  "total_cost": "0.05",
  "service_charge": "0"
}
'''

IMAGE_FOLDER_DIR = '/Users/hazmei/Documents/repositories/gemini-test-python/images/'

def extract_data_from_gemini(api_key, model, image_path):
    genai.configure(api_key=api_key)

    # Model variants
    # https://ai.google.dev/gemini-api/docs/models/gemini#model-variations
    model = genai.GenerativeModel(model)
    image = PIL.Image.open(image_path)

    response = model.generate_content([PROMPT, image])

    result = json.loads(response.text.strip("```json").strip())
    return(result)

def main():
    gemini_model = 'gemini-1.5-flash-8b'
    gemini_api_key = os.environ['GEMINI_API_KEY']
    image_path = IMAGE_FOLDER_DIR + 'receipt_2.jpg'

    receipt_data = extract_data_from_gemini(gemini_api_key, gemini_model, image_path)
    print(receipt_data)

if __name__ == '__main__':
    main()
