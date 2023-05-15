import unittest
import sys
from io import StringIO
from redirect import Redirect


class RedirectTest(unittest.TestCase):
    def test_stdout_redirect(self):
        # Prepare the redirect target
        redirect_output = StringIO()

        with Redirect(stdout=redirect_output):
            print("Hello, stdout!")

        # Get the redirected output
        redirected_text = redirect_output.getvalue()

        self.assertEqual(redirected_text.strip(), "Hello, stdout!")

    def test_stderr_redirect(self):
        redirect_output = StringIO()

        with Redirect(stderr=redirect_output):
            raise ValueError("Hello, stderr!")

        redirected_text = redirect_output.getvalue()

        self.assertIn("ValueError: Hello, stderr!", redirected_text)

    def test_stdout_stderr_redirect(self):
        # Prepare the redirect targets
        redirect_stdout = StringIO()
        redirect_stderr = StringIO()

        with Redirect(stdout=redirect_stdout, stderr=redirect_stderr):
            print("Hello, stdout!")
            raise ValueError("Hello, stderr!")

        redirected_stdout = redirect_stdout.getvalue()
        redirected_stderr = redirect_stderr.getvalue()

        # Assert the redirected outputs
        self.assertEqual(redirected_stdout.strip(), "Hello, stdout!")
        self.assertIn("ValueError: Hello, stderr!", redirected_stderr)


if __name__ == "__main__":
    unittest.main()
