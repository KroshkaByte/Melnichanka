# Melnichanka

This is a brief description of your project.

## Table of Contents

- [How to run the project](#how-to-run-the-project)
- [Project Description](#project-description)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## How to run the project

1. Install Docker and Docker Compose
To get started with Melnichanka, you will need to have Docker and Docker Compose installed on your system. You can follow the instructions for your operating system here and here.

Once you have Docker and Docker Compose installed, follow these steps to start the project:

   - Clone the repository:

```git clone https://github.com/KroshkaByte/Melnichanka.git
```
   - Change to the project directory:

```cd melnichanka
```
   - Start the database:

```docker-compose up -d db
```
   - Start the project:

```docker-compose up -d web
```
   - Open your web browser and navigate to http://localhost:8000 to access the application.

## Project Description

Melnichanka is a web application designed to facilitate the process of submitting shipment applications to consignees. The application generates a package of documents required for shipment based on user input, including information about goods, brands, factories, and packages.

The application is intended to be used by companies that need to submit shipment applications on a regular basis. By using Melnichanka, companies can streamline the process of generating the necessary documents, reduce errors, and save time and resources.

The application includes a user-friendly interface that allows users to easily enter data and generate documents. The interface is designed to be intuitive and easy to use, even for users with little or no technical experience.

Melnichanka is built using modern web technologies, including Django, a popular web framework for Python. The application is containerized using Docker and Docker Compose, making it easy to deploy and scale.

Overall, Melnichanka is a powerful and flexible tool that can help companies save time and resources when submitting shipment applications. By automating the process of generating documents, Melnichanka can help companies reduce errors, improve efficiency, and focus on their core business.


## Usage

To use Melnichanka, follow these steps:

   - Enter the required information about the goods, brands, factories, and packages.
   - Click the "Generate Documents" button to generate the package of documents required for shipment.
   - Review the generated documents and make any necessary edits.
   - Download the documents in the desired format (e.g., PDF, Word, Excel).
   - Submit the documents to the consignee as required.

## Testing

To run the tests, navigate to the root directory of the project (where the manage.py file is located) and run the following command:

```
pytest
```

- To run tests for a specific model, such as Goods, use the following command:

pytest goods/tests/

## Contributing

We welcome contributions to Melnichanka. To contribute, follow these steps:

   - Fork the repository.
   - Create a new branch for your changes.
   - Make your changes and commit them to your branch.
   - Submit a pull request.

We will review your pull request and provide feedback as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more information. (./license)
