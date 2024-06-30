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
[![pre-commit](https://img.shields.io/badge/precommit-0.2-FAB040?style=flat&logo=precommit&logoColor=white)](https://pre-commit.com/)
[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet?style=flat)](https://flake8.pycqa.org/en/latest/)
[![mypy](https://img.shields.io/badge/mypy-checked-blue?style=flat)](https://mypy-lang.org/)

# Melnichanka

## Table of Contents

- [Project Description](#project-description)
- [How to run the project](#how-to-run-the-project)
- [Usage](#usage)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Description

***Melnichanka: Simplifying Shipment Application Submissions***

Melnichanka is a web application designed to streamline the process of submitting shipment
applications. It automates the generation of necessary documents based on user input, covering
details such as goods, brands, factories, and packages.

***Key Benefits:***

- Efficiency: Automates document generation to save time and resources.
- Accuracy: Reduces errors associated with manual data entry.
- Accessibility: User-friendly interface ensures ease of use, suitable for all levels of technical
  proficiency.
- Convenience: Simplifies the submission process, even for users with minimal technical experience.

***Technological Foundation:***

- Built with Django: Utilizes the robust Django framework for Python, ensuring reliability and
  flexibility.
- Containerized with Docker: Deployed using Docker and Docker Compose, enabling easy scalability
  and
  deployment.

***Target Audience:***

Designed for companies needing to submit shipment applications regularly.
Ideal for organizations seeking to enhance efficiency, minimize errors, and optimize resource
allocation.

***Conclusion:***

Melnichanka empowers companies by automating the creation of shipment documents, enabling them to
focus on core business activities. It stands as a powerful tool for improving operational
efficiency and streamlining document submission processes.

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

- [Configure .env](#environment-configuration)

<p>

- Start the project from root directory:

```sh
docker-compose up -d --build
```

- Open your web browser and navigate to http://localhost:80 to access the application.

#### Environment Configuration

You need to manually update this secret in your `.env` file each time it changes.

Additionally, create a `.env` file in the root directory based on the provided `.env.example`. Fill
in your own data and rename the file to `.env`.

Please note that the Django secret key used in the `.env.example` is just an example. You can
generate a new key using the following command:

   ```sh
   from django.core.management.utils import get_random_secret_key
   
   print(get_random_secret_key())
   ```

## Usage

To use Melnichanka, follow these steps:

- Enter the required information about the goods, brands, factories, and packages.
- Click the `Generate Documents` button to generate the package of documents required for shipment.
- Verify all the data and create an archive with documents.
- Download the archive of documents in Excel format.
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
