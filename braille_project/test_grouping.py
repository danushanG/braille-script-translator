# test_grouping.py

# Simulated detected dot centers (x, y)
dot_centers = [
    (100, 100),
    (100, 140),
    (100, 180),
    (130, 100),
    (130, 140),
    (130, 180)
]

# Group into 6-dot Braille cells
grouped_cells = [dot_centers[i:i + 6] for i in range(0, len(dot_centers), 6)]

print("\nGrouped Braille Cells:")
for idx, cell in enumerate(grouped_cells):
    print(f"Cell {idx + 1}: {cell}")
