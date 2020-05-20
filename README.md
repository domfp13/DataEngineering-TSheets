# DataEngineering-TSheets

This is the Tsheets project, here we are extracting data from the TSheets REST API, cleaning, transforming, this is a cloud based project that is completely Serverless.

### Objective

> Enhance the current process that runs on AppScripts with a better
> and robust solution

### Tech

List of technologies used for this project

* Cloud funtions (Python 3.7)
* Cloud Storage
* Cloud Scheduler
* Cloud Source Repositories (Mirror GitHub)

### Local Testing

Requires [Python](https://docs.conda.io/en/latest/miniconda.html) v3.7+ to run.

Install the dependencies

```sh
$ cd DataEngineering-TSheets
$ conda create -n tsheets python=3.7
$ conda activate myenv
$ pip install --upgrade -r requirements.txt
$ # Open etl/GenericFunctions.py and deactivate decorators and add Token
$ python main_test.py
```

#### Building for source
if new lib added to the project update requirements.txt
```sh
$ pip freeze --local > requirements.txt
```

### Docker
GCP builds the container therefore the requirements.txt needs to be provided

```sh
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./your-daemon-or-script.py" ]
```

### Todos

 - 
 - 
 
## Authors
* **Luis Fuentes** - *2020-05-20*