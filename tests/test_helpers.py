import unittest

from helpers import get_payload


class TestGetPayload(unittest.TestCase):
    def test_get_unreplace_payload(self):
        expected = {
            "email": "${email}",
            "accountName": "UA Account",
            "recaptchaToken": "random",
        }

        actual = get_payload(payload="ensure_account")

        assert expected == actual

    def test_get_payload(self):
        expected = {
            "email": "test@canonical.com",
            "accountName": "UA Account",
            "recaptchaToken": "random",
        }

        actual = get_payload(
            payload="ensure_account",
            replaces={"email": "test@canonical.com"},
        )

        assert expected == actual
