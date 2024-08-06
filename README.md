Local Business Locator
Overview
The Local Business Locator is a Django/DRF project that allows users to find and view local businesses on a map. Utilizing the Google Maps API, this project provides an interactive and user-friendly interface to search for businesses by location, view detailed information, and get directions. The application is built with Django for the backend and Django Rest Framework (DRF) for creating the API endpoints.

Features
Interactive Map Integration: Use Google Maps to display businesses' locations on an interactive map.
Business Search: Search for businesses based on location, type, or name.
Detailed Business Information: View detailed information about each business, including address, contact details, and operating hours.
Directions: Get directions to the selected business using Google Maps.
User-Friendly Interface: Easy-to-use interface for a seamless user experience.
Installation

Clone the Repository:
git clone https://github.com/yourusername/local-business-locator.git

cd local-business-locator


Create a Virtual Environment:
python -m venv venv


source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables:
Create a .env file in the root directory and add your Google Maps API key:
GOOGLE_MAPS_API_KEY=your_google_maps_api_key


Run Migrations:
python manage.py migrate


Start the Development Server:
python manage.py runserver


Usage
Access the Application: Open your browser and go to http://127.0.0.1:8000/.
Search for Businesses: Use the search functionality to find businesses based on your criteria.
View Business Details: Click on a business to view more details and get directions.
Contributing
