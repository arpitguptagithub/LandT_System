# Multilingual Automation System README

## Project Overview

This project aims to develop a multilingual automation system for level and pressure control using Google Assistant and Raspberry Pi. The system leverages natural language processing (NLP) techniques using the SpaCy library to interpret user commands. Additionally, basic Python libraries such as Matplotlib and Pandas are utilized for version control of the system's data. To ensure security, the project employs libraries like hashlib and secrets for password storage, safeguarding against cybersecurity threats.

## Features

- Multilingual support for user interaction.
- Automation of level and pressure control systems.
- Integration with Google Assistant for voice commands.
- Raspberry Pi implementation for physical control.
- NLP processing using SpaCy for interpreting user instructions.
- Version control of system data using Matplotlib and Pandas.
- Secure password storage using hashlib and secrets.

## Contributors 
 [Arpit Gupta]{https://github.com/arpitguptagithub} , [Chirag Kotian]{https://github.com/ChiragKotian} , [Sudhakar V]{https://github.com/sudhakarv1}

## Installation Instructions

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-repo-url.git
    ```

2. Install required Python libraries:

    ```bash
    pip install spacy matplotlib pandas
    ```

3. Set up SpaCy language models:

    ```bash
    python -m spacy download en
    python -m spacy download fr
    # Add additional languages as needed
    ```

4. Run the system:

    ```bash
    python main.py
    ```

## Usage

1. Ensure the Raspberry Pi is properly connected to the control systems.
2. Activate Google Assistant and initiate communication with the automation system.
3. Issue voice commands in the preferred language for level and pressure control.
4. Monitor system responses and feedback.
5. Utilize version control features to track changes and maintain data integrity.
6. Ensure passwords are securely stored and managed using provided libraries.

## Contributing

Contributions to the project are welcome. Please follow these guidelines when contributing:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with descriptive commit messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to the contributors and maintainers of the libraries and tools used in this project. Their efforts have been invaluable in its development.
