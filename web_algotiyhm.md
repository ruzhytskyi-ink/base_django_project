I. Preparing to launch a project

Write specificatin of aplication: (bussiness plan)
    a) Goals of project
    b) Functionality
    c) Appearance (зовнішній вигляд)
    d) user interface

_______________________________________________________________________________________________________________________

Our specification:
    1. app_name: Learning Log
    2. functionality: user can keep a log of interestd topics and create entires (записи) while learning every topic
    3. Homepage include:
        a. Description of the site
        b. Invites user to Sign in or Log in
        c. Once log in, user will be able to:
            i.create new topics
            ii. add new entires
            iii. read and edit current entires

_______________________________________________________________________________________________________________________

II. Algorithm of creating web-app:

1. Creating of virtual environment
    a) Create directory of app
    b) navigate to this directory in terminal mode and use next command:

python -m venv venv (name of virtual env)

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser (for Windows to access venv mode)

venv/Scripts/activate (deactivate - to leave virtual env)

2. Choose venv python enterpreter in your code editor (VS code):
    i. Ctrl+Shift+P (або Cmd+Shift+P на Mac), 
    ii. enter Python: Select Interpreter 
    iii. choose enterpreter that is located in your project venv (наприклад, ./.venv/Scripts/python.exe)

3. Installation of Django 

pip install django

4. Creating the project (main files: manage.py, settings.py, urls.py)

django-admin startproject learning_log .

5. Creating of Datebase

python manage.py migrate

6. Check development server:

python manage.py runserver

7. Creating app in your project (models.py, admin.py, views.py)

python manage.py startapp learning_logs

8. Start Work with app
    1. Definition of models 'Topic' (look at: ...app/models.py)
        a. Full list of django model filds you can see here: https://docs.djangoproject.com/en/6.0/ref/models/fields/
    2. Model activating (project_dir/settings.py -> add app_name like 'learning_logs' to INTALLED_APPS )
    3. Every time when you change data which "app" manages,
       you need to update the datebase, so make next steps:
        i. change ... app/'models.py'
        ii. python manage.py makemigrations app_name
        iii. python manage.py migrate

9. Admin site
    1. Creating of superuser
        python manage.py createsuperuser
    2. Import and Register model at admin panel (look at ...app/admin.py)
    3. Run server and Add topics by admin panel at http://localhost:8000/admin/
    
10. Update model.py to add new model for entering information in your topics using 'many-to-one' relationship
    1. Definition of new model 'Entry' (look at: ...app/models.py)
    2. Update datebase with makemigrations and migrate
    3. Import and Register model 'Entry' at admin panel (look at ...app/admin.py)

11. Creating Homepage (It include: 1.defining URLs, 2. writing views 3. writing templates )
    1. URL comparison (edit project/urls.py and then app/urls.py)
    2. Write Views (func with arguments (request obj, template) + can be data procesing)
    3. Write template:
        a. make dir in app_dir(like learning_logs)/templates/the same name of app(like learning_logs)/index.html

12. Creating the 'base.html' template from which all templates in this project will inherit (Parent template) 

13. Creating of other pages (in ours case we'll create 2 pages for output data:
    1. list of topics (http://.../topics)
        a. Create scheme of URLs (usual)
        b. Write func of view (description look at views.py)
        c. Create template  - html-page 'topics.html' and add it's path to base.html  
    2. List of entires on a specific topic (http://.../topics/topic_id/)
    (representation of Topic-name and list of entires of current topic)
        a. Create scheme of URLs with ID-atribute 
        b. Write view func which receive additional id-atribute (description look at views.py)
        c. Create template - html-page 'topic.html' and add it's path to topics.html 
        (Here we can see Django MVT design pattern)
            і. | - Django filter func for Django-templates
            ii. entry.date_added |date:'M d, Y H:i' - formats the date directly within the template
            iii. entry.text|linebreaks - converts \n to HTML (<p>, <br>)

_______________________________________________________________________________________________________________________
_Template Note: 
Між topic.id (in template topics.html) і topic_id (in logic views.py) існує не очевидна, але важлива відмінність. 
- Вираз topic.id перевіряє тему та отримує значення відповідного ідентифікатора. 
- Змінна topic_id містить посилання на цей ідентифікатор у коді. 
Якщо ви зіткнетеся з помилками під час роботи з ідентифікаторами, переконайтеся, що ці вирази використовуються правильно 

_______________________________________________________________________________________________________________________
_Design patterns note: 
Main goal of this pattern is to separate the business logic (what the programme does in views.py) from 
the interface (what the user sees in templates), which simplifies the scaling, testing and maintenance of projects

        Key differences by design patterns
Characteristic      |    MVC     |   MVT (Django)   |
Logic               | Controller |      View        |
Interface           |    View    |     Template     |
Data                |    Model   |      Model       |
_______________________________________________________________________________________________________________________


III. User accounts

14. Editing data (The same as in 11 and 13 points, but with new modul - 'forms.py') 
    i. Adding Page for users to _Create Topics_
        - create 'forms.py' in directory with models.py:
            > import models and define class TopicForm as ModelForm object to provide functionality of forms, 
        -make url comparison, 
        -view func (process 2 situations:
            >  original queries for the new_topic page (empty form)
            >  process data sent on form and redirect user back
        -create template, 
        -add link to new_topic at topics template)
    ii. Adding Page for users to _Create topic entires_:
        - update forms.py and add class EntryForm which is more specific
        - update url with specification (the entire must be linked to a specific topic)
        - update view with func new_entire with specification
        - create template and add link on it to topic.html
    iii. Adding Page for users for _Editing enteries_:
        - update url
        - update view with new func
        - create template and add it's link to topic.html

_______________________________________________________________________________________________________________________
Note: at this level we can use functionality of web-site but can't save changes.
_______________________________________________________________________________________________________________________

15. Creating of user accounts (Registration and authorization system)

    1. Creating new app 'users'
        python manage.py startapp users
    2. Add users app to 'INSTALLED_APPS' in project settings
    3. Including users URLs into root file urls.py
    4. Loggining page:
        a. creating urls.py in new app and update it with default django authentication URLs (which include 'login' 
        and 'logout' named schemas)
        b. Creating 'login' template (login.html) which may be located in dir 'registration' which must be 
        in dir 'learning_log/users/templates/registration/'  (django looking for it by  default auth)
        c. Creating log in link in base.html and test is it work
    5. Adding log out form in base.html
        e. Creating of Logout confirmation page with creatinh of template 'logged_out.html' (notification of logging out)
_______________________________________________________________________________________________________________________
Note: Logging out may not work becouse app 'users' can be located under default admin app of django 
in INSTALLED_APPS in settings
_______________________________________________________________________________________________________________________

    5. Registartion page:
        a. Update users urls.py with adding of registration path and our new view of this page
        b. Update users views.py with creating a new func register()
        c. Creating 'register.html' template
        d. Adiing registration link to base.html

_______________________________________________________________________________________________________________________
NOTE: This registration system allows any user to create as many Learning Log accounts as they wish. 
!!! However, some systems require the user to confirm their application by sending an email, to which the user must reply. With this approach, the system will create fewer spam accounts than the simplest system in our example. 
_______________________________________________________________________________________________________________________

16. Editing data II (work with data which belong sollely to user)
    1. Restricting access using decorator '@login_required'
        a. Import decorator func 'login_required' into learning_logs views and write decorator before func 'topics'
        b. Update settings with link-path (LOGIN_URL) for redirection
        c. Restriction access in learning_logs (need to decide which pages will have unlimitted access and which - NO)
            i. We will allow unlimited access for home, registration and logging in pages 
            and restrict access for all other pages with decorator 'login_required' in views
    2. Linking data to specific users (establish a connection only with the data at the top level of the hierarchy; 
                                        the lower-level data will follow automatically.)
        a. Update Topic model (add the foreign key relationship to the user)
        b. Identification of existing users
            i.  python manage.py shell
                from django.contrib.auth.models import User     
                User.objects.all()                      -> look at all users
                for user in User.objects.all():     
                    print(user.username, user.id)       -> to use id for connecting of topics with user
        c. Make migration of database
            i. python manage.py makemigrations learning_logs
            ii. Python propose to connect the Topic model(all existing topics) to a specific owner 
                                                        (in our case we choose __1__ for admin))
            iii. write 1 (admins id) or another id of user
            iiii. Make migration 
                    python manage.py migrate
            iiiii. Check with shell to ensure that the migration went as planned:
                >>> from learning_logs.models import Topic      
                >>> for topic in Topic.objects.all():
                        print(topic, topic.owner)       -> check all topic for owners

                        """if error try to reoper the shell"""
_______________________________________________________________________________________________________________________
NOTE: It is also possible to clear DB and rebuilt new DB with:
python manage.py flush
_______________________________________________________________________________________________________________________

17. Restricting (обмеження) access to topics (user sea only his topics)
    1. Update func Topics() in learning_views/views with '.filter(owner=request.user)'
    (it check if topic owner user match with responded curreent user)

18. User topic protection
    - 1. If you try to log in as not as admin go by link  http://localhost:8000/topics/1/ (you can see topic of another users)
    1. to resolve this problem we will provide checking before receiving data in func topic()
        a. Update func topic() and import Http404 (If the topic does not belong to the current user, 
                                                    an Http404 exception is thrown)
19. Protecting the edit_entry page
    1. Provide the same with func edit_entry

20. Linking new topics to the current user
    0. At present, the page for adding new topics is not fully functional because 
       it does not link new topics to a specific user.
    1. Resolve this problem with updating func 'new_topic()' in views.py:
        i. Gain access to current user data through request object 