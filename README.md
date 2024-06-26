# PMEventropy

Compute in python entropy for process mining describe in Back, C.O., Debois, S. & Slaats, T. Entropy as a Measure of Log Variability. J Data Semant 8, 129–156 (2019). https://doi.org/10.1007/s13740-019-00105-3 ([the article](https://rdcu.be/dJMwH))

This project is inspired by https://github.com/backco/eventropy

## Installation

    pip install pmentropy

## Get started

First import the XES file

    import pmentropy
    logs = pmentropy.read_file("path", flatten=False)

Then compute an entropy

    entropy1 = pmentropy.kNN_entropy(logs, k=3, p=2)
    entropy2 = pmentropy.global_block_entropy(logs k=3, p=2)

### Import with pm4py

with a DataFrame

    import pmentropy
    from pm4py.read import read_xes

    df = read_xes("path")
    logs = pmentropy.read_DataFrame(df, flatten=False)

    entropy1 = pmentropy.kNN_entropy(logs, k=3, p=2)

\
trace by trace if you already read by stream

    import pmentropy
    from pm4py.streaming.importer.xes import importer as xes_importer

    stream = xes_importer.apply("path", variant=xes_importer.xes_trace_stream)
    next_trace, logs = pmentropy.read_trace_by_trace(flatten=False)
    for trace in stream:
        next_trace(trace)

    entropy1 = pmentropy.kNN_entropy(logs, k=3, p=2)

## Documentation

Parse file

- read_file(file_path: str, flatten=False)
- read_trace_by_trace(flatten=False)

Entropy

- trace_entropy(logs)
- prefix_entropy(logs)
- unique_trace(logs)
- k_block_entropy(logs, k: int)
- global_block_entropy(logs)
- kL_entropy(logs, p: int)
- kNN_entropy(logs, k: int, p: int)
- lempel_ziv_entropy_rate(logs)
- k_block_entropy_rate_ratio(logs, c)
- k_block_entropy_rate_diff(logs, c)
- unique_trace(logs)
