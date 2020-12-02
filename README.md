# wix-projects
## Author  
  
[LekamCharity](https://github.com/LekamCharity/wix-projects.git)  
  
# Description  
This is an application whereby users can rate their favorite websites and also display them.

## User Story  

* Allow users to read register and login.
* Allows users to post,view and rate posted projects. 
* Display submitted projects.


## Live Link

 https://wixapplication.herokuapp.com/

## Figma Link
```
https://www.figma.com/file/TKcES6XuIO8pnvJhV4BUNf/wix-projects?node-id=0%3A1
```
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/LekamCharity/wix-projects.git
```
##### Navigate into the folder 

* cd wix-projects

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django 3.1.3]
* [Heroku]  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  

## Contact Information   
If you have any question or contributions, please email me at [lekamcharity@gmail.com]  

### License
  [MIT](https://github.com/LekamCharity/wix-projects/blob/master/License) Copyright (c) 2020 Lekam Charity