# VESSL-Server

### html-generation-demo

## Description
On this branch you can find a Django server which will in future be able to digest [PQ9EGSE](https://github.com/DelfiSpace/PQ9EGSE) frames and display these as a webpage. It achieves this by automatically generating the webpage HTML code with the Python package [TemPy](https://github.com/Hrabal/TemPy).


## Setting up the webserver (on Unix-like OS)
To test the server, do the following:
1. Ensure Python 3.6+ is installed.
2. Ensure the Python packages [Django](https://www.djangoproject.com/download/) and [TemPy](https://github.com/Hrabal/TemPy) are installed.
3. Git clone this repository.
```
$ git clone https://github.com/DelfiSpace/VESSL-Server/tree/html-generation-demo
```
4. Navigate to the root of the repository and start the server using: 
```
$ python3 manage.py runserver
```
5. Open your web browser and connect to *localhost:5000/downlink/*.

You should now see something like this:
![alt text](./progress.png?raw=true)


## Planned Upgrades
Before this module will be integrated into the VESSL server, a number of issues will need to be solved:
- [X] How to integrate code as a Django webservice?
- [ ] Fix issue with table pair not aligning horizontally
- [ ] How to pass on special characters to the HTML generator? Python's Unicode specification ( u/N{________}) does not seem to work, and using the HTML codes (&#___) seems to copy the characters verbatim because the table generator adds extra characters to the ampersand. For example, try to put the degree symbol in the unit section of the table. How to do this in future, and how to ensure that math symbols/greek characters/other can be added easily by future devs/users.
- [ ] Fetch a complete XTCE frame from Github and compare the layout to the basic dict that is used.
- [ ] Modify the code to copy the values
- [ ] Add a function that allows for a new frame to be compared to the current rendered frame, and value indexing such that the values that need updating can be isolated and changed separately.
- [ ] Muck around with header/footer/body in CSS so that all elements are responsive for a variety of resolutions.
- [ ] Figure out whether the TU Delft has a standard CSS layout, and if not, define one for VESSL.
- [ ] Look into "upload"-frame and investigate how buttons can be implemented.
- [ ] Shove the implementation into a Django layout and turn it into a web application
- [ ] Write code testing routines along Django implementation.


## Authors
 - Johan Monster - https://github.com/Hans-Bananendans/

## License
This project is licensed under the GPL-3.0 License.