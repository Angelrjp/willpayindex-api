# WillPayIndex API

_This is flask application of Will Pay Index which performs the calculation to predict if the user paid their obligations on time_

### Installation 🔧

_Go to terminal and inside the project directory, and type the following commands:_

_Installation of necessary libraries_
```
pip install -r .\requirements.txt
```

_Create folder for database_
```
mkdir database
```

_Creation of the database_

```
python -c "from app import db; db.create_all()"
```

_Insert data into database_
```
python insert_data.py
```

### Deploy 📦

_Run the app_

```
flask run
```

### How to use

_The server is started and now go to your browser and open URL:_
```
http://localhost:5000/api/v1/users/<user_id>/will-pay-index/
```

_Example:_
```
http://localhost:5000/api/v1/users/1/will-pay-index/
```

### Endpoint for testing the api

_Endpoint_
```
https://willpayindex-api.herokuapp.com/api/v1/users/<user_id>/will-pay-index/
```

_Example_
```
https://willpayindex-api.herokuapp.com/api/v1/users/1/will-pay-index/
```



