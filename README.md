# Algorithm Complexity Experiment

Python coursework exploring the runtime of nested loops with logarithmic increments. The script compares measured runtimes with an analytical growth expression on log-log axes.

**Stack:** Python standard library · Matplotlib

## Run

```bash
git clone https://github.com/abiy8/6212_Project1.git
cd 6212_Project1
python -m venv .venv
# Activate .venv for your operating system.
pip install matplotlib
python complexity_experiment.py
```

The script measures `n = 100, 200, 400, 800, 1600` and opens a plot. Large values can take substantial time. `reportlab` and `python-docx` from the old instructions are not imported by the implementation.

## Interpretation

This is an empirical coursework experiment. The plotted theoretical expression is not normalized to the timing measurements, despite its existing legend label; compare growth trends rather than absolute magnitudes. Timings use `time.time()` and one run per input, with no repeated-run confidence estimates. The script executes when imported, so run it as a script.
