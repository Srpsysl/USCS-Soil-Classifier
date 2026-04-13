# USCS-Soil-Classifier
A Python tool to automate geotechnical soil classification using USCS standards.

Calculates Plasticity Index (PI) and A-Line. Then based on the USCS Soil classification table, it calculates conditions based on the inputs of the user.

## How to Use
Run the script in any Python environment. The terminal will prompt you to enter the standard geotechnical lab results:
1. Percentage passing the No. 200 sieve
2. Percentage passing the No. 4 sieve
3. Liquid Limit (LL) & Plastic Limit (PL)
4. Oven-dried LL (for organic checks)
5. Coefficients of Uniformity (Cu) and Curvature (Cc)

## Example Output
```text
Passed Material Percentage (No. 200): 8
Passed Material Percentage (No. 4): 85
LL: 25
PL: 22
Enter Oven Dried Liquid Limit: 25
Cc: 1
Cu: 3

Soil class is SP-SM
