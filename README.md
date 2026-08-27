# MemoryMind: A Lightweight Statistical Framework for Memory Forensic Artifact Prioritization Using Relational Evidence Correlation

## Research Objective

The objective of this project is to demonstrate a simple approach for prioritizing memory forensic artifacts based on evidence scores and relational correlation.

## Research Methodology

The project uses simulated memory forensic artifacts. Each artifact is assigned an evidence score and a relational correlation score. A weighted calculation is then used to calculate the priority score and rank the artifacts.

## Result

The results show that `malware.exe` received the highest priority score of 0.935, followed by `unknown.exe` with a score of 0.785. The results are saved in `recognition_result.csv` and visualized using a bar chart.

## Conclusion

The prototype demonstrates how statistical scoring and relational evidence correlation can be used to prioritize memory forensic artifacts. Although simulated data is used, the approach can later be extended using real memory dumps and forensic tools such as Volatility 3.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt