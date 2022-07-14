__all__ = ("QApi",)


class QApi:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def test(self):
        print("yes working...")
