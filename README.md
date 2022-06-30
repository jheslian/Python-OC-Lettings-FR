
# Orange County Lettings Website
	
	
### Objective
Scale a Django Application Using Modular Architecture where as the improvement of the application follows:
1.  Reduction of various technical debts on the application
2.  Redesign of the modular architecture
3.  Added CI/CD pipeline using CircleCI and Heroku
4.  Application monitoring and error tracking via Sentry.
  
# Development
  
### Prerequisites
- Git
- SQLite3 CLI
- Python interpreter, version 3.6 or higher
  
In the rest of the local development documentation, it is assumed that your OS shell's `python` command runs the Python interpreter above (unless a virtual environment is enabled).
  
### macOS / Linux
  
#### Clone repository
  
- `git clone https://github.com/jheslian/Python-OC-Lettings-FR.git`
  
#### Create the virtual environment
  
- `cd Python-OC-Lettings-EN`
- `python -m venv venv`
- `apt-get install python3-venv` (If the previous step has errors with a package not found on Ubuntu)
- Activate environment `source venv/bin/activate`
- Confirm that the `python` command is running the Python interpreter in the virtual environment
`which python`
- Confirm Python interpreter version is 3.6 or higher `python --version`
- Confirm that the `pip` command runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`
  


#### Run the application
  ***Note:*** `DEBUG=False` must be modified to `DEBUG=True` on the oc_lettings_site/setting.py when on development.
- `cd /path/to/Python-OC-Lettings-EN`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser.
- Confirm that the site is working and navigable (you should see multiple profiles and locations).
  
#### Linting
  
- `cd /path/to/Python-OC-Lettings-EN`
- `source venv/bin/activate`
- `flake8`
  
#### Unit tests
  
- `cd /path/to/Python-OC-Lettings-EN`
- `source venv/bin/activate`
- `pytest`
  
#### Database
  
- `cd /path/to/Python-OC-Lettings-EN`
- Open a `sqlite3` shell session
- Connect to `.open oc-lettings-site.sqlite3` database
- Show tables in `.tables` database
- Show columns in profiles table, `pragma table_info(profiles_profile);`
- Run a query on the profile table, `select user_id, favorite_city from
 profiles_profile where favorite_city like 'B%';`- `.quit` to quit
  
#### Admin Panel
  
- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`

  
### Windows
  
Using PowerShell, as above except:
  
- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` - Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Run the application using Docker:
Prerequiqites:
- [Docker](https://www.docker.com/)

### Build an image/container
1. Run `docker build --tag <dockerhub name>:<tagname>`
2. Run `docker run --name <container name> -d -p 8000:8000 <dockerhub name>:<tagname>`

### Create image in dockerhub with image built locally
1. Run `docker login`
2. Run `docker tag <dockerhub name>:<tagname> <dockerhub username>/<dockerhub name>:<tagname>`
3. Run `docker push <dockerhub username>/<dockerhub name>:<tagname>`
***Check dockerhub account for image created***

### Use image from dockerhub 
Pull the image from dockerhub and run application locally  
1. Run `docker pull <dockerhub username>/<dockerhub name>:<tagname>`
2. Run `docker run -p 8000:8000 <dockerhub username>/<dockerhub name>:<tagname>`

# Deployment
## Prerequisites
-   [GitHub](https://github.com/) - clone the application
 -  [Docker](https://www.docker.com/)  - application container
-   [CircleCI](https://circleci.com/) - a continuous integration and continuous delivery platform
-   [Heroku](https://www.heroku.com/)  - simplest path to get the application run in the market
-   [Sentry](https://sentry.io/welcome/) - a crash reporting platform that provides you with "**real-time insight into production deployments"**

***Note:*** Make sure that there are no project name "oc-lettings-proj" in your heroku account

Configuration:
Create the environment variables in circle ci project with the following name:

[![Screenshot-2022-06-27-at-20-37-47.png](https://i.postimg.cc/WzxkkMkQ/Screenshot-2022-06-27-at-20-37-47.png)](https://postimg.cc/BPcbWPNg)


Then:
-   Navigate to  `https://<heroku-app-name>.herokuapp.com`  in a browser
-   Navigate to  `https://<heroku-app-name>.herokuapp.com/sentry-debug`, this should trigger an error in sentry
-   Login to the admin panel `https://<heroku-app-name>.herokuapp.com/admin` using above credentials
