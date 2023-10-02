# advarisk_project

1. Install Django and other required packages
   $ pip install django  

2. Then install the dependencies:
   $ pip install -r requirements.txt

3. Once `pip` has finished downloading the dependencies:
4. Navigate to the project directory:
   $ cd project
5. Create a virtual environment:
   $ python -m venv venv
   
6. Activate the virtual environment:
   $ source venv/bin/activate
7. Install dependencies:
   $ pip install -r requirements.txt
8. Apply database migrations:
   $ python manage.py makemigrations
   $ python manage.py migrate 
   
9. Set up your News API key:
   Replace 'your_api_key' with your News API key.
10. Run the development server:
   $ python manage.py runserver
   
11. Open your browser and go to http://127.0.0.1:8000/ to access the application.


#Project Structure
news_search:

Contains Django app files.
Models: Keyword and SearchResult.
Views: search_news and view_results.
Templates: search.html and results.html.
news_api.py: Module for fetching news from the News API.
settings.py:

Configuration file for Django settings, including the News API key.
requirements.txt:

Lists the project dependencies.



#Time Taken
I spent approximately 20 hours building this project.



#Experience
Working on this project was a great experience. I enjoyed building a Django web application and integrating it with an external API. The process of creating models, views, and templates, as well as handling user authentication, was both educational and satisfying. Implementing features like preventing frequent searches and avoiding duplicate keywords added an extra layer of complexity and made the project more interesting.
