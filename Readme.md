# Django REST Framework API Basics
## Overview
Welcome to the Django REST Framework (DRF) API Basics project! This project is designed to introduce fundamental concepts in API development using Django and DRF. It covers the implementation of Model Viewsets for efficient CRUD operations, Model Serializers for data validation and serialization, and the application of permissions to control API access.

## Features
1. **Model Viewsets**
    - **CRUD Operations:** Utilize Django's Model Viewsets to handle Create, Retrieve, Update, and Delete operations for your API endpoints.
    - **Routing:** Automatically routes URLs based on the provided queryset and serializer class.
2. **Model Serializers**
    - **Data Serialization:** Implement Model Serializers to convert complex data types, such as Django models, into native Python data types and then into JSON, ensuring data integrity and format consistency.
    - **Validation:** Validate incoming data against predefined rules using serializer fields and methods.
3. **Permissions**
    - **Access Control:** Explore different permission classes provided by DRF to manage who can view, create, update, or delete data through API endpoints.
    - **Authentication:** Secure your API endpoints with authentication mechanisms such as Token Authentication or Session Authentication.
## Getting Started
### Prerequisites
Ensure you have the following installed before proceeding:

- Python 3.x
- Django
- Django REST Framework

## Installation
- Clone the Repository:
```
git clone https://github.com/Muneeb1030/DRF_Basics.git
cd DRF_Basics/
```
- Install Dependencies:
```
pip install -r requirements.txt
```
- Run Django Migrations:
```
python manage.py migrate
```
- Start the Django Development Server:
```
python manage.py runserver
```
- Access the API:

- Navigate to `http://localhost:8000/api/` to explore the available API endpoints.
- Use tools like Postman or curl to interact with the API endpoints and perform CRUD operations.
## Project Structure
- **/profile_app/:** Contains Django app files.
- **/profile_app/models.py:** Defines Django models used in the API.
- **/profile_app/serializers.py:** Contains Model Serializers for data validation and serialization.
- **/profile_app/views.py:** Implements Model Viewsets and API logic.
- **/profile_api/settings.py:** Configuration file where app settings and DRF configurations are defined.
## Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, please fork the repository and submit a pull request.
