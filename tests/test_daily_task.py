import unittest
from unittest.mock import Mock, patch

import requests

from daily_task import concise_error_message, mark_daily_task


class DailyTaskTests(unittest.TestCase):
    @patch("daily_task.requests.post")
    def test_marks_wxread_with_timeout(self, post):
        response = Mock()
        post.return_value = response

        self.assertTrue(mark_daily_task("Y"))

        post.assert_called_once_with(
            "https://geng.tang.ee/mark_daily_task",
            json={"column": "WXRead", "content": "Y"},
            timeout=10,
        )
        response.raise_for_status.assert_called_once_with()

    @patch("daily_task.requests.post")
    def test_mark_failure_is_swallowed(self, post):
        post.side_effect = requests.Timeout("timed out")

        self.assertFalse(mark_daily_task("Y"))

    def test_error_message_is_concise_and_single_line(self):
        message = concise_error_message(RuntimeError("first line\nsecond line"), max_length=30)

        self.assertEqual(message, "RuntimeError: first line se...")


if __name__ == "__main__":
    unittest.main()
