import pandas as pd

dwarf_data = pd.read_csv("dwarf_stars.csv")

dwarf_data.dropna(inplace=True)

dwarf_data['Mass'] = dwarf_data['Mass'].astype(float)
dwarf_data['Radius'] = dwarf_data['Radius'].astype(float)

dwarf_data['Radius'] = dwarf_data['Radius'] * 0.102763

dwarf_data['Mass'] = dwarf_data['Mass'] * 0.000954588

dwarf_data.to_csv("cleaned_dwarf_stars.csv", index=False)

bright_star_data = pd.read_csv("brightest_stars.csv")

merged_data = pd.merge(dwarf_data, bright_star_data, on="Star_name")

merged_data.to_csv("merged_star_data.csv", index=False)
