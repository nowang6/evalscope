from evalscope.perf.main import run_perf_benchmark
from evalscope.perf.arguments import Arguments

task_cfg = Arguments(
    parallel=[1, 5, 10, 15, 20],
    number=[10, 10, 20, 30, 40],
    model='/workspace/Qwen2.5-VL-7B-Instruct',
    url='http://127.0.0.1:8860/v1/chat/completions',
    api='openai',
    dataset='random',
    min_tokens=3000,
    max_tokens=3000,
    prefix_length=0,
    min_prompt_length=3000,
    max_prompt_length=3000,
    tokenizer_path='/root/weights/Qwen2.5-VL-7B-Instruct',
    extra_args={'ignore_eos': True}
)
results = run_perf_benchmark(task_cfg)