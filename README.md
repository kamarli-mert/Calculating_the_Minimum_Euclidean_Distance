# Calculating the Minimum Euclidean Distance

This Python script calculates the Euclidean distance between two points in a 2D space. Users can input coordinates, and the script processes the input to validate and calculate the distance using the Euclidean distance formula.

## Features

- **User Input**: Prompts the user to enter points in the format `(x, y)`. Input is validated to ensure it meets the required format.
- **Distance Calculation**: Computes the Euclidean distance between two valid points.
- **Error Handling**: Handles incorrect input formats and ensures the program continues running smoothly.

## How It Works

### 1) Input Handling
- The user is prompted to enter points in the format `(x, y)`.
- The script strips unnecessary characters, splits the input, and converts the values to integers.
- If the input is invalid (e.g., incorrect format or non-integer values), an error is displayed, and the user is prompted to enter the data again.

### 2) Calculation
- Once two valid points are entered, the script computes the Euclidean distance using the formula:
  
  ```python
  distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
  ```

### 3) Output
- The calculated distance is displayed to the user.

## Example Usage
```bash
Enter a point (x, y) or 'q' to exit: (3, 4)
Enter a point (x, y) or 'q' to exit: (7, 1)
Minimum distance between two points: 5.0
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/mertkamarli/Calculating_the_Minimum_Euclidean_Distance.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Calculating_the_Minimum_Euclidean_Distance
   ```

3. Run the script:
   ```bash
   python3 distance_calculator.py
   ```

## Requirements
- Python 3.x
- `math` module (built-in in Python)

## Contributing
Contributions are welcome! If you'd like to improve the script or add new features, feel free to:
- Fork the repository
- Create a new branch
- Submit a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Note
Ensure that inputs follow the `(x, y)` format and contain valid integers to avoid errors during processing.
