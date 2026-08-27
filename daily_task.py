import logging

import requests


MARK_DAILY_TASK_URL = "https://geng.tang.ee/mark_daily_task"
MARK_TIMEOUT_SECONDS = 10


def concise_error_message(exc, max_length=200):
    """Return a short, single-line description suitable for the task API."""
    message = " ".join(str(exc).split()) or exc.__class__.__name__
    description = f"{exc.__class__.__name__}: {message}"
    if len(description) > max_length:
        return f"{description[:max_length - 3]}..."
    return description


def mark_daily_task(content, timeout=MARK_TIMEOUT_SECONDS):
    """Mark WXRead's result without changing the job's own outcome."""
    try:
        response = requests.post(
            MARK_DAILY_TASK_URL,
            json={"column": "WXRead", "content": content},
            timeout=timeout,
        )
        response.raise_for_status()
        logging.info("WXRead 每日任务状态标记成功。")
        return True
    except Exception as exc:
        logging.error("WXRead 每日任务状态标记失败：%s", exc)
        return False
