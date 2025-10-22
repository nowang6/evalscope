from evalscope.run import run_task

task_cfg = {
    "model": "Qwen3-30B-A3B-Instruct-2507",
    "datasets": ["gsm8k", "cmmlu","tool_bench"],
    "api_url": "http://127.0.0.1:1025/v1/chat/completions",
    "api_key": "empty",
    "eval_type": "openai_api",
    "eval_batch_size": 64
}
run_task(task_cfg=task_cfg)