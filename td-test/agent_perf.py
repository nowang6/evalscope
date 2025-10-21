rom evalscope.perf.main import run_perf_benchmark
from evalscope.perf.arguments import Arguments

task_cfg = Arguments(
    parallel=[1, 10, 40, 50, 100, 200],
    number=[10, 20, 80, 100, 200, 400],
    model='Qwen3-30B-A3B-Instruct-2507',
    url='http://127.0.0.1:1025/v1/chat/completions',
    api='openai',
    dataset='random',
    min_tokens=512,
    max_tokens=512,
    prefix_length=0,
    min_prompt_length=512,
    max_prompt_length=512,
    tokenizer_path='/root/weights/Qwen3-30B-A3B-Instruct-2507',
    extra_args={'ignore_eos': True}
)
results = run_perf_benchmark(task_cfg)