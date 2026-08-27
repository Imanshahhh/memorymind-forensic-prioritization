import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Artifact": [
        "malware.exe",
        "unknown.exe",
        "svchost.exe",
        "explorer.exe"
    ],
    "Evidence_Score": [0.95, 0.80, 0.25, 0.10],
    "Relational_Correlation": [0.90, 0.75, 0.30, 0.20]
}

df = pd.DataFrame(data)

df["Priority_Score"] = (
    df["Evidence_Score"] * 0.7
    + df["Relational_Correlation"] * 0.3
)

df = df.sort_values(
    by="Priority_Score",
    ascending=False
)

df.to_csv("recognition_result.csv", index=False)

print("MemoryMind Forensic Artifact Prioritization Results")
print(df)

plt.figure(figsize=(8, 5))

plt.bar(
    df["Artifact"],
    df["Priority_Score"]
)

plt.title("MemoryMind Artifact Similarity Score")
plt.xlabel("Memory Artifact")
plt.ylabel("Similarity / Priority Score")

plt.tight_layout()
plt.savefig("similarity_chart.png")

plt.show()

print("\nFiles generated successfully.")