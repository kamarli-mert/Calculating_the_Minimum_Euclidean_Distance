This Python script allows users to calculate the Euclidean distance between two points in a 2D space. 
The script takes input in the form of coordinates, processes the input to validate and extract the coordinates, 
and then calculates the distance using the Euclidean distance formula.

Features
	*User Input: The script prompts the user to enter points in the format (x, y). The input is processed and validated to ensure correctness.
	*Distance Calculation: Once two valid points are provided, the script calculates the Euclidean distance between them.
	*Error Handling: The script includes error handling to manage incorrect input formats and ensure the program runs smoothly.

How It Works
	1)Input Handling:
	*The user is prompted to enter points in the format (x, y).
	*The script strips any unnecessary characters, splits the input, and maps the values to integers.
	*If the user enters an invalid format or non-integer values, the script will catch the error and prompt the user to enter the 		data again.

	2)Calculation:
	*After two points are entered, the script computes the Euclidean distance using the formula:
			distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

	3)Output:
	*The calculated distance is displayed to the user.
			## Example Usage
			Enter a point (x, y) or 'q' to exit: (3, 4)
			Enter a point (x, y) or 'q' to exit: (7, 1)
			Minimum distance between two points: 5.0
