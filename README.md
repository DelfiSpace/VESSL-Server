# Channels-WS-Example

This branch provides a very basic example of how communication between the Python package [websockets](https://websockets.readthedocs.io/en/stable/) and a [Django Channels](https://channels.readthedocs.io/en/stable/) server may work.

To run this example, first start the Django server by running `python manage.py runserver` in the `Server` directory.
Then, you can simply run `example-application` in the `Client` directory.

This example sends a Python dictionary to the server, which then modifies it by changing one of its values and adding another key/value pair before sending it back to the client application.
