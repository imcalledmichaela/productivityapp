# productivityapp

Use the following commands to create a virtual environment so that you will be able to run flask. 

This command creates a folder called venv which stores all your python dependencies.
>`python -m venv venv`

To activate the virtual environment:
1. Windows
>`venv\Scripts\activate.bat`

2. Linux or MacOS
> `source venv/bin/activate`

Next you need to install the dependencies using
>`pip install -r requirements.txt`

Finally, to run the flask application, use
>`flask run`
or 
>`python app.py`