# Solar Trade Optimizer

## Project Overview

The **Solar Trade Optimizer** is a Python program designed to optimize trade routes between solar systems. Each solar system is represented as a node in a graph, and the connections between them (jumpgates) are represented as edges. The goal is to calculate the most profitable trade circuit for transporting commodities between systems, factoring in costs such as ship operational expenses and transport capacity.

### Features
- Capture commodity price data from screen using OCR.
- Graph-based representation of solar systems and jumpgates.
- Path optimization using heuristics to maximize profit while minimizing costs.
- Supports a variety of commodities: Food, Clothing, Metal, Plastic, Equipment, Medical, Industrial, Electronics, Heavy Metals, and Luxury Goods.
- Flexible design for easy extension.

## Installation

### Requirements

- Python 3.8 or higher
- Tesseract OCR engine installed and available in your system's PATH. You can download it [here](https://github.com/tesseract-ocr/tesseract/wiki).

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/solar_trade_optimizer.git
    cd solar_trade_optimizer
    ```

2. **Set up a virtual environment (optional)**:
   If you're using Conda:
    ```bash
    conda create --name solar_trade_optimizer python=3.8
    conda activate solar_trade_optimizer
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tesseract OCR engine**:
    - Download and install from [Tesseract OCR Downloads](https://github.com/tesseract-ocr/tesseract/wiki).
    - Make sure to add Tesseract to your PATH.

## Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```

2. **Test the environment**:
    There is a test script `environment_test.py` to verify that key components like `networkx` and `pytesseract` are working correctly.
    ```bash
    python environment_test.py
    ```

3. **Project Structure**:
    - `main.py`: Entry point for running the trade optimization logic.
    - `solar_trade/`: Core logic for the project, including graph management, data capture, pathfinding, and ship operations.
    - `tests/`: Unit tests for each module in the project.

## Contributing

Feel free to open issues and submit pull requests if you'd like to contribute to the project. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
