# Mail_Sent

A simple Python script (`main.py`) to send emails using SMTP.

## How to Use

1. Open `main.py` and enter your SMTP server, email address, and your Gmail app password (not your regular password).
2. Run:
    ```bash
    python main.py
    ```
    ## Requirements

    - Python 3.x
    - Internet connection
    - Access to an SMTP server (e.g., Gmail)

    ## Setup

    1. Clone or download this repository.
    2. Update the SMTP settings in `main.py` with your credentials.

    ## Security Note

    - Use an app-specific password for Gmail.
    - Do not share your credentials or commit them to version control.

    ## Example

    ```python
    # main.py
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    password = "your_app_password"
    ```

    ## Troubleshooting

    - Make sure "Allow less secure apps" is enabled for your email provider (if required).
    - Check your internet connection.
    - Verify SMTP server and port.
