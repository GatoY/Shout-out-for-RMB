# Loan System

A website with simple loan system.

##Features: 
	
* This system use some features to determine whether we could loan to individuals. These features are including their age, credit, whether got a guarantee, income, have a house or not.

* I use decision tree to train the dataset and record the tree model. 

* The users can upload their information thus the system will give the result whether they get the loan.
	

####Set-up: pip install -r requirements.txt 


####set database: 

* Firstly, change 'USER', 'PASSWORD' to ur own accounts in settings.py;
* Then, create new database in ur own Mysql database;

####run
On ur own machine

    python manage.py runserver