// Get the display element
const display = document.getElementById("display");

// Function to append values to the display
function appendValue(value) {
    display.value += value;
}

// Function to clear the display
function clearDisplay() {
    display.value = "";
}

// Function to evaluate the expression
function calculate() {
    try {
        // Evaluate the expression and update the display
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }
}
