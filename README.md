# TaskName: VariantControl

## Tech-Stack: 
FastAPI: Used FastApi which a python backend framework 
MongoDb: A No-SQL database that stores data in BSON format

## Getting started:
- Clone the repo: ``` git clone https://github.com/SamayMody/VariantControl.git ```
- Install the requirements: ``` pip install -r requirements.txt ```
- Start the servers: ``` uvicorn main:app --reload ```
- Visit FastAPI Interactive API docs to test the API's : ``` http://127.0.0.1:8000/docs ```

## Routes:
- POST /upload/product = To add Products with multiple variants
- GET /get/product = To get data by just querying Product name
- GET /get/variants = To get all products which have that variant type
- UPDATE /update/product = To update the variants of a particular product
- DELETE /delete/product/variant = To delete the particular product variant
- DELETE /delete/product/{product} = To delete the complete product along with all its variants

## ScreenShots : 
![Screenshot (45)](https://github.com/SamayMody/VariantControl/assets/113875363/ad362c2e-a462-4de6-93d4-459484946a6e)

![Screenshot (46)](https://github.com/SamayMody/VariantControl/assets/113875363/234b43fd-9cf0-42da-9cea-7b437f0f9e4e)
