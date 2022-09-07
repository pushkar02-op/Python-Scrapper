<!-- # Fast Api Backend for React App

Full Backend for React Highradius Callworkboard app using Fast Api, Docker, Python.

## Run Locally

Clone the project

```bash
  git clone https://github.com/pushkar02-op/React-Highradius-Backend.git
```

## Using Docker Compose

```bash
  docker-compose up -d --build
```

To delete everything

```bash
  docker-compose down
```

## Using uvicorn

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn callworkboard:app --reload
```

## 🔗 Links

[Open in local](http://localhost:8008/)

[To test in Docs](http://localhost:8008/docs)

## API Reference

#### Test

```http
  GET /
```

#### Fast Api Docs

```http
  GET /docs
```

#### React app path to get data

```http
  GET /cms/tovo/v1/getUserCallWorkBook.do
```

## Tech Stack

**Client:** React, Redux,

**Server:** FastApi, Python

## Prerequisites

1. Python
2. virtualenv preffered

## Notes To Remember

Create Virtualenv

```bash
virtualenv myenv
```

Activate

```bash
myenv\Scripts\activate
```

To create requirements.txt

```bash
pip freeze > requirements.txt
```

## Deployed on Heroku

### Steps :-

1. Download Heroku Cli

2.

```bash
  heroku login
```

3.

```bash
  heroku create
```

4.

```bash
  heroku git:remote -a {name of app}
```

5.

```bash
  git add .
```

6.

```bash
  git commit -m "first deploy"
```

7.

```bash
  git push heroku main
```

Deployement Done on Heroku -->
