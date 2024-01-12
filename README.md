# Automated Email Sender

## Description

The Automated Email Sender is a Python program that streamlines the process of sending personalized emails to a list of users. Leveraging file handling and API integration, the program reads a template and a user details file from the local file system. It then automates the email-sending process, replacing placeholders in the template with user names and sending personalized emails to each user.

## Features

- **File Handling**: Reads a template and a user details file from the local file system.

- **API Integration**: Utilizes an email-sending API to automate the process.

- **Personalized Emails**: Replaces placeholders in the template with user names for a personalized touch.

## How it Works

1. **Template and User Details**: The program reads a template file and a user details file from the local file system.

2. **API Integration**: Utilizes an email-sending API to automate the email-sending process.

3. **Personalization**: Replaces placeholders in the template with user names from the user details file.

4. **Email Sending**: Sends personalized emails to each user listed in the file.

## Getting Started

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/automated-email-sender.git
    cd automated-email-sender
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API Key**:

    Obtain an API key for the email-sending service and configure it in the `config.json` file.

4. **Prepare Files**:

    - Create a template file with placeholders for user names.
    - Prepare a user details file containing a list of users and their details.

5. **Run the Program**:

    ```bash
    python email_sender.py
    ```

6. **Automated Email Sending**:

    The program will read the template and user details, replace placeholders, and send personalized emails.

## API Configuration

Ensure you have the necessary API key and configure it in the `config.json` file for the email-sending functionality.

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or encounter any issues, please follow the contribution guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License.

Automate your email sending with personalized touches using the Automated Email Sender!
