print("Animal Feed Chemistry Analyzer")
feed_type = input("Enter the type of feed")
feed_intake = float(input("Enter the feed intake in kg: "))
parameters =(
"Moisture content in %",
"Crude protein in %", 
"Crude fiber in %",
 "Crude fat in %",
 "Ash content in %"
)
feed_composition = []
for parameter in parameters:
    value = float(input(f"Enter the value for {parameter.strip()}: "))
    feed_composition.append(value)
dry_matter = 100 - feed_composition[0]  # Moisture content
dry_matter_intake = (feed_intake * dry_matter) / 100
protein_intake = (dry_matter_intake * feed_composition[1]) / 100  # Crude protein
fiber_intake = (dry_matter_intake * feed_composition[2]) / 100  # Crude fiber
fat_intake = (dry_matter_intake * feed_composition[3]) / 100  # Crude fat
ash_intake = (dry_matter_intake * feed_composition[4]) / 100  # Ash content
result_name = ["Dry matter",
              "Dry matter intake",
              "Protein intake", 
              "Fiber intake", 
              "Fat intake",
              "Ash intake"
                ] 
result_value = [dry_matter,
                 dry_matter_intake,
                 protein_intake,
                 fiber_intake,
                fat_intake,
                ash_intake
                ]
for name, value in zip(result_name, result_value):
    print(f"{name}: {value:.2f}")
