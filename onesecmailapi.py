import requests

class OneSecMailApi:
    def __init__(self) -> None:
        self.api = "https://www.1secmail.com/api/v1/"
        self.session = requests.Session()
        
    def generate_random_mail(self, amount: int) -> list[str]:
        """
        Generating random email addresses
        
        Args:
            amount (int): Number of email addresses to generate
              
        Returns:
            list[str]: A list of generated email addresses
        """
        response = self.session.get(f"{self.api}?action=genRandomMailbox&count={amount}")
        response.raise_for_status()
        return response.json()
    
    def domain_list(self) -> list[str]:
        """
        Checking available domains
        
        Returns:
            list[str]: A list of available domains
        """
        response = self.session.get(f"{self.api}?action=getDomainList")
        response.raise_for_status()
        return response.json()
    
    def get_messages(self, username: str, domain: str) -> list[dict]:
        """
        Checking your mailbox
        
        Args:
            username (str): The username of the mailbox
            domain (str): The domain of the mailbox
        
        Returns:
            list[dict]: A list of messages
        """
        response = self.session.get(f"{self.api}?action=getMessages&login={username}&domain={domain}")
        response.raise_for_status()
        return response.json()
    
    def fetch_single_message(self, username: str, domain: str, message_id: int) -> dict:
        """
        Fetching a single message
            
        Args:
            username (str): The username of the mailbox
            domain (str): The domain of the mailbox
            message_id (int): The ID of the message
            
        Returns:
            dict: The message details
        """
        response = self.session.get(f"{self.api}?action=readMessage&login={username}&domain={domain}&id={message_id}")
        if "Message not found" in response.text:
            return {"error": True, "message": "Message not found"}
        response.raise_for_status()
        return response.json()
    
    def download_attachment(self, username: str, domain: str, message_id: int, attachment_name: str, encoding: str = "UTF8") -> bytearray:
        """
        Downloading an attachment
            
        Args:
            username (str): The username of the mailbox
            domain (str): The domain of the mailbox
            message_id (int): The ID of the message
            attachment_name (str): The name of the attachment
            encoding (str): The encoding to use (default is "UTF8")
            
        Returns:
            bytearray: The attachment data
        """
        response = self.session.get(f"{self.api}?action=download&login={username}&domain={domain}&id={message_id}&file={attachment_name}")
        response.raise_for_status()
        return bytearray(response.content)
