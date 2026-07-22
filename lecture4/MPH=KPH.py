print(f"{'KPH':<10}{'MPH':<10}")
print("-" * 20)
for kph in range(60, 131, 10):
    mph = kph * 0.6214

    print(f"{kph:<10}{mph:<10.1f}")