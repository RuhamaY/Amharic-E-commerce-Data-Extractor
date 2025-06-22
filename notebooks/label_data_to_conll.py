import pandas as pd

df = pd.read_csv("preprocessed_data.csv")

output_file = open("labeled_data.conll", "w", encoding="utf-8")

print("Starting manual labeling for 30 messages.")
print("Label using: B-Product, I-Product, B-PRICE, I-PRICE, B-LOC, I-LOC, O")

for idx, row in df.head(30).iterrows():
    print(f"\nOriginal Message [{idx + 1}]: {row['original']}")
    tokens = eval(row['tokens']) if isinstance(row['tokens'], str) else row['tokens']

    for token in tokens:
        label = input(f"{token}: ").strip()
        output_file.write(f"{token} {label}\n")

    output_file.write("\n")

output_file.close()
print("✅ Saved to labeled_data.conll")
