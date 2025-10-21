from evalscope.run import run_task

task_cfg = {
    "model": "Qwen3-30B-A3B-Instruct-2507",
    "datasets": ["gsm8k", "arc"],
    "api-url": "http://127.0.0.1:1025/v1/chat/completions",
    "api-key": "empty",
    "eval-type": "service",
    "limit": 5
}
run_task(task_cfg=task_cfg)