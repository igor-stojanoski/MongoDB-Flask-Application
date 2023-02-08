# MongoDB Flask Application

This Flask app cleans the data into an SQLite3 database and imports it encrypted into a Mongo database. The application contains two main functions. The first function cleans the data from the SQLite3 database, reads the data with the Pandas module, and cleans the column with company names from unwanted characters with re (regular expression) and Cleanco modules. Then, with the Cryptography module, the data is encrypted and written to the Mongo database with the PyMongo module. The second function decrypts and displays the data from the Mongo database in a frontend built with Bootstrap, JavaScript, and jQuery that gives the appearance and functionality to the Flask application from where we can enter a custom value range to display the data from the Mongo database in JSON format or a table with search functionality.

## Getting Started

Before importing this project to your Python workspace, it is necessary to make sure the prerequisite steps are properly done in your development environment. The installation procedure described in this documentation will assume you already have Python installed on your computer.

#### Prerequisites

+ A Python Editor of your choice
For this project, the [PyCharm](https://www.jetbrains.com/pycharm/) IDE and [Visual Studio Code](https://code.visualstudio.com/) were used for development, but the same is not required to correctly deploy the application itself.

+ Install the virtual environment package
Virtual Environment (virtualenv) is a tool to create isolated Python environments. The virtualenv command creates a folder that contains all the necessary executables to use the packages that a Python project would need. The same can be installed as described in [this link](http://docs.python-guide.org/en/latest/dev/virtualenvs/) through the following command:


```bash
pip install virtualenv
```
---
#### Installing

The steps below will guide you through the project installation.
The following commands should be executed in your computer console in the project folder:

+ Clone the project to your local repository workspace
+ Create a virtual environment for the imported application through the following command:
---
> Windows command:

```
virtualenv <Virtual Environment name>
```
> Linux command:

```
python3 -m venv venv
```
---
+ Activate your virtual environment with the command

> Windows command:
```
<Virtual Environment name>\Scripts\activate
```
> Linux command:

```
source venv/bin/activate
```

+ With the virtual environment properly activated, install the plugins available in the requirements.txt file through the command:

```
pip install -r requirements.txt
```
This process should enable your application to be deployed on a local server for test purposes.


## Deployment

With the webapp.py file and the virtual environment activated, the python application should run through the following command:

>Windows/Linux command:

```
python webapp.py

```
The same will enable the project to be accessed by your web browser through a URL displayed by the mentioned command execution.

## Technologies Used

### Languages

+ [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - build up the layout and content of the application.
+ [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - add custom styling and override Bootstrap styling to fit with the theme of the website.
+ [JavaScript](https://www.javascript.com/) - to add interactive functionalities to the app
+ [Python](https://www.python.org/) - to build back-end functionalities handling data and database interaction.

### Programs and Tools

+ [Visual Studio Code](https://code.visualstudio.com/) - the code editor being used to build the project.
+ [Git](https://git-scm.com/) - the built-in Git feature in VS Code was used for version control and push to GitHub.
+ [Github](https://github.com/) - GitHub is used to store project code remotely.
+ [SQLite3](https://sqlite.org/) - the database used to clean the data into plain text.
+ [MongoDB](https://www.mongodb.com/) - the database being used to store encrypted data and queries.

### Frameworks and Libraries

+ [Bootstrap v5.1](https://getbootstrap.com/) - the responsive front-end framework to build the layout and style the app.
+ [jQuery](https://jquery.com/) - a JavaScript library used for the simplicity of traversing HTML documents and manipulation, event handling, and Ajax.
+ [Flask](https://palletsprojects.com/p/flask/) - a micro web framework written in Python which is the barebone of this stock management app.
+ [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Python distribution containing tools for working with MongoDB.
+ [Pandas](https://pandas.pydata.org/) - Python library used to work with the SQLite3 database.
+ [Cryptography](https://cryptography.io/en/latest/) - Python library used to encrypt and decrypt data.
+ [Cleanco](https://pypi.org/project/cleanco/) - Python package that processes company names, providing cleaned versions of the names.
+ [re](https://docs.python.org/3/library/re.html) - Python library used to clean the data from the SQLite3 database.