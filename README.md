Instructions for running the application

Export the app with
``` export FLASK_APP=src/app.py```

Run the app with 
```flask run```

The server is running locally on http://127.0.0.1:5000

Application health endpoint: http://127.0.0.1:5000/health

Application metrics endpoint: http://127.0.0.1:5000/metrics

Application Database Results endpoint: http://127.0.0.1:5000/database_data

To run unit tests go to the `/src/tests` folder and run
```python -m test_all_unit_tests```

To run integration tests go to the `/src/tests` folder and run
```python -m test_all_integration_tests```

