import re


class PhoneNumber:
    PATTERN = re.compile(
        """
        ^\+?1? # International country code
        \s* # Optional whitespace
        \(?([2-9]{1}[0-9]{2})\)? # Area code
        [.\s-]* # Optional separator
        ([2-9]{1}[0-9]{2}) # Local number
        [.\s-]* # Optional separator
        ([0-9]{4}) # Subscriber number
        \s*$ # Optional whitespace
        """,
        re.VERBOSE,
    )

    def __init__(self, number):
        match = re.match(PhoneNumber.PATTERN, number)
        if not match:
            raise ValueError("Phone number not valid")
        self.area_code, self.exchange_code, self.subscriber_number = match.groups()

    @property
    def number(self):
        return self.area_code + self.exchange_code + self.subscriber_number

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
