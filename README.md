# Python 3.X

## Usage

```py
from onesecmailapi import OneSecMailApi

if __name__ == "__main__":
    api = OneSecMailApi()

    # Generate a random email address
    random_mail = api.generate_random_mail(amount=1)

    # Get a list of available domains
    domains = api.domain_list()

    # Fetch messages for a specific email address
    messages = api.get_messages(username="7u582a", domain="laafd.com")

    # Fetch a single message by its message ID
    single_message = api.fetch_single_message(username="7u582a", domain="laafd.com", message_id=1909355985)

    # Download an attachment from a specific message
    attachment = api.download_attachment(username="7u582a", domain="laafd.com", message_id=1909355985, attachment_name="file.pdf", encoding="UTF8")
```
