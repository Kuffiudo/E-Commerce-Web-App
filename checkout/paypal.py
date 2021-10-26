import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AR8n7NUoezpbwL0b1W9yM-lKWO4ehu8Bxf-mGJxvZp97HIEPL-QTq-Rg4r53dNmJ5_3xMF15P3j-jy4l"
        self.client_secret = "EP_1lQz5oloJwkuEf6psfmKSiuo8FUQ6NMtwqqlW7Xf89uwYn_8PvAjDVHUcK54qEU7_ceQrpZLmzTUi"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)