import unittest
from unittest.mock import patch

import main


class MainTests(unittest.TestCase):
    @patch("main.mark_daily_task")
    @patch("main.run_job")
    def test_marks_success_after_job_completes(self, run_job, mark_daily_task):
        main.main()

        run_job.assert_called_once_with()
        mark_daily_task.assert_called_once_with("Y")

    @patch("main.mark_daily_task")
    @patch("main.run_job", side_effect=RuntimeError("read failed"))
    def test_marks_error_and_preserves_original_failure(self, run_job, mark_daily_task):
        with self.assertRaisesRegex(RuntimeError, "read failed"):
            main.main()

        mark_daily_task.assert_called_once_with("RuntimeError: read failed")


if __name__ == "__main__":
    unittest.main()
