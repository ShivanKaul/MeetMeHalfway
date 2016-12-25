# MeetMeHalfway-Backend

### To set up

#### Pip
Make sure you have >= Python 2.7 installed. Then, install pip from here: https://pip.pypa.io/en/latest/installing/. 

#### Virtualenv
Run:

`[sudo] pip install virtualenv`

Good tutorial on why we need virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

To start developing, make sure you have virtualenv running:

`virtualenv venv`

This will create an `venv/` folder. Run:

`source venv/bin/activate`

This will activate virtualenv. To deactivate (don't do this right now! When you want to stop developing do this):

`deactivate`

Now, you're ready to develop!

#### Install dependencies
Run `pip install -r requirements.txt`. This should install all the dependencies. Whenever you add a new library or something from pip, add it to `requirements.txt`. More info about requirements.txt here: https://pip.pypa.io/en/stable/user_guide/#requirements-files 

### Running

Simply do: `python backend/server.py`. This should start up the backend API server. To interact with it, I'd suggest downloading something like [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop). This is what I'd use to test:





