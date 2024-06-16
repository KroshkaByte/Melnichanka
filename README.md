[![Python](https://img.shields.io/badge/Python-3.12.2-3776AB?style=flat&logo=Python&logoColor=yellow)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15.1-092E20?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.3-336791?style=flat&logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7.2.5-DC382D?style=flat&logo=Redis&logoColor=white)](https://redis.io/)
[![Celery](https://img.shields.io/badge/Celery-5.4-37814A?style=flat&logo=Celery&logoColor=white)](https://docs.celeryq.dev/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.13.3-FF6600?style=flat&logo=RabbitMQ&logoColor=white)](https://www.rabbitmq.com/)
[![Docker](https://img.shields.io/badge/Docker--2496ED?style=flat&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-3.17-269539?style=flat&logo=Nginx&logoColor=white)](https://www.nginx.com/)
[![Psycopg2-binary](https://img.shields.io/badge/Psycopg2--binary-2.9.9-4169E1?style=flat)](https://pypi.org/project/psycopg2-binary/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-21.2-FFD700?style=flat&logo=Gunicorn&logoColor=white)](https://gunicorn.org/)
[![pytest](https://img.shields.io/badge/pytest-8.0.2-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Ruff](https://img.shields.io/badge/Ruff-0.3-FCC21B?style=flat&logo=ruff&logoColor=white"/)](https://github.com/astral-sh/ruff)
[![SimpleJWT](https://img.shields.io/badge/SimpleJWT-5.3.1-orange?style=flat&logo=jwt&logoColor=white)](https://github.com/jazzband/djangorestframework-simplejwt)

# Melnichanka

## Table of Contents

- [How to run the project](#how-to-run-the-project)
- [Project Description](#project-description)
- [Usage](#usage)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## How to run the project

1. Install [`Docker`](https://www.docker.com/)
   and [`Docker Compose`](https://docs.docker.com/compose/)
   To get started with Melnichanka, you will need to have [Docker](https://www.docker.com/)
   and [Docker Compose](https://docs.docker.com/compose/) installed on your system. You can follow
   the instructions for your operating system here and here.

Once you have [Docker](https://www.docker.com/)
and [Docker Compose](https://docs.docker.com/compose/) installed, follow these steps to start the
project:

- Clone the repository:

```sh
git clone https://github.com/KroshkaByte/Melnichanka.git
cd Melnichanka
```

- Start the project from root directory:

```sh
docker-compose up -d --build
```

- Open your web browser and navigate to http://localhost:80 to access the application.

## Project Description

Melnichanka is a web application designed to facilitate the process of submitting shipment
applications to consignees. The application generates a package of documents required for shipment
based on user input, including information about goods, brands, factories, and packages.

The application is intended to be used by companies that need to submit shipment applications on a
regular basis. By using Melnichanka, companies can streamline the process of generating the
necessary documents, reduce errors, and save time and resources.

The application includes a user-friendly interface that allows users to easily enter data and
generate documents. The interface is designed to be intuitive and easy to use, even for users with
little or no technical experience.

Melnichanka is built using modern web technologies, including `Django`, a popular web framework for
Python. The application is containerized using Docker and Docker Compose, making it easy to deploy
and scale.

Overall, Melnichanka is a powerful and flexible tool that can help companies save time and
resources when submitting shipment applications. By automating the process of generating documents,
Melnichanka can help companies reduce errors, improve efficiency, and focus on their core business.

## Usage

To use Melnichanka, follow these steps:

- Enter the required information about the goods, brands, factories, and packages.
- Click the `Generate Documents` button to generate the package of documents required for shipment.
- Review the generated documents and make any necessary edits.
- Download the documents in the desired format (e.g., PDF, Word, Excel).
- Submit the documents to the consignee as required.

## Database Pre-population

To pre-populate the database with some initial data, you can use the provided script. This script
utilizes the `Faker` library to generate fake data.

Please follow the steps below to run the script:

- Navigate to the root directory of the project in your terminal.

- Run the following command:

```sh
python3 manage.py runscript faker_script
```

Make sure `django-extensions` is installed and added to `INSTALLED_APPS` in your Django settings.

This command will execute the `faker_script` script, which will then populate the database with the
generated data.

Please note that the data generated by the Faker library is random and does not represent any real
information.

Ensure that your `virtual environment` is activated before running the commands, if you're using
one.

## Documentation

API documentation is available through Swagger UI and ReDoc.

- [Swagger UI](https://dev-lymar.github.io/Melnichanka/melnichanka_swager_ui)
- [ReDoc](https://dev-lymar.github.io/Melnichanka/melnichanka_redoc)

For local access, navigate to [`Swagger UI`](http://localhost:8000/api/schema/swagger-ui/)
and [`ReDoc`](http://localhost:8000/api/schema/redoc/) in your browser after starting the project.

## Testing

To run the tests, navigate to the root directory of the project (where the manage.py file is
located) and run the following command:

```sh
pytest .
```

or

```sh
python3 -m pytest .
```

- To run tests for a specific application (such as goods, logistics, users, etc.) use the following
  command:

```sh
pytest goods
pytest logistics
pytest users
pytest clients
pytest makedoc
```

## Contributing

We welcome contributions to Melnichanka. To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Update your branch from the main repository:
    ```sh
    git fetch upstream
    git merge upstream/main
    ```

5. Submit a pull request.

We will review your pull request and provide feedback as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
