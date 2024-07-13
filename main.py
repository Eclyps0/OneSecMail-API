from onesecmailapi import OneSecMailApi

if __name__ == "__main__":
    api = OneSecMailApi()
    random_mail = api.generate_random_mail(amount=1)
    domains = api.domain_list()
    messages = api.get_messages(username="7u582a", domain="laafd.com")
    single_message = api.fetch_single_message(username="7u582a", domain="laafd.com", message_id=1909355985)
    attachment = api.download_attachment(username="7u582a", domain="laafd.com", message_id=1909355985, attachment_name="file.pdf", encoding="UTF8")