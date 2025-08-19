# analysis.py
# Author: 23f1002560@ds.study.iitm.ac.in
# Marimo interactive notebook for variable relationships
# This notebook demonstrates:
# 1. Variable dependencies
# 2. Interactive slider widget
# 3. Dynamic markdown output

import marimo as mo

# Cell 1: Input widget (independent variable)
slider = mo.ui.slider(1, 10, value=5)
mo.md(f"### Adjust the slider below:\n{slider}")

# Cell 2: Dependent variable (calculated based on slider value)
# Data flow: value from Cell 1 → computation here
x = slider.value
y = x ** 2   # Example: quadratic relationship

# Cell 3: Dynamic markdown output (depends on Cell 2)
# Data flow: values of x and y are displayed interactively
mo.md(f"""
## Relationship Demo  

- Selected value (x): **{x}**  
- Computed value (y = x²): **{y}**  

{'⭐' * x}
""")
