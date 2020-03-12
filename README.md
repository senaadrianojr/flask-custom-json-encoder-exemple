# flask-custom-json-encoder-exemple
A custom JSON Encoder for flask projects.

# (UNDER DEVELOPMENT)

This is an exemple how to implement a custom json encoder for flask projects. I developed this solution for encoding an mongodb collection where occur error at the flask json while try to convert a dictionary of type ObjectId to string (default method used in flask json).

## Step by step:

- Implement a class that extends flask json JSONEncoder and override super class default method (see encoder.py file);
- In the application configuration file, define the configuration for the json encoder to implement the custom encoder class (see the app.py file);
