
# **PyDataLens Installation Guide**

This guide explains how to install and set up the **PyDataLens** package for automatic exploratory data analysis (EDA), data cleaning, and visualization.

---

## **Prerequisites**

### 1. **Python Version**
- Ensure you have **Python 3.6 or later** installed on your system.
- You can check your Python version by running:
  ```bash
  python --version
  ```

### 2. **Pip**
- Make sure you have `pip` (Python's package manager) installed and updated:
  ```bash
  pip install --upgrade pip
  ```

---

## **Installation Steps**

### **Step 1: Clone the Repository**
Download the PyDataLens repository from GitHub:
```bash
git clone https://github.com/yourusername/PyDataLens.git
cd PyDataLens
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**
Set up a virtual environment to isolate your Python dependencies:
```bash
python -m venv pydatalens_env
source pydatalens_env/bin/activate  # On Windows: pydatalens_env\Scripts\activate
```

### **Step 3: Install the Package**
Run the following command to install the PyDataLens package and its dependencies:
```bash
pip install -e .
```

---

## **Dependencies**

PyDataLens requires the following Python packages:

- **pandas**: For data manipulation
- **numpy**: For numerical operations
- **matplotlib**: For data visualizations
- **seaborn**: For advanced visualizations

All required dependencies will be installed automatically during the installation process. If you encounter issues, you can manually install them:
```bash
pip install pandas numpy matplotlib seaborn
```

---

## **Testing the Installation**

After installation, you can verify the setup by running the following commands:

### **1. Check the Installation**
Run this Python command to check if the package is installed:
```bash
python -c "import pydatalens; print('PyDataLens is installed successfully!')"
```

### **2. Run Tests**
Navigate to the `tests` folder and run the test scripts:
```bash
cd tests
python test_eda.py
python test_cleaning.py
python test_visualizations.py
```

---

## **Examples**

Once installed, you can try the package using the example script provided:

### **Run the Example**
Navigate to the `examples` folder and execute the script:
```bash
cd examples
python example_usage.py
```

---

## **Common Installation Issues**

### **1. Missing Dependencies**
If some dependencies fail to install, try installing them manually:
```bash
pip install -r requirements.txt
```

### **2. Permission Issues**
If you encounter permission-related errors, try:
```bash
pip install --user -e .
```

---

## **Uninstalling PyDataLens**

To remove the package from your system:
```bash
pip uninstall pydatalens
```

---

## **Support**

If you encounter any issues or need help, please open an issue in the GitHub repository:
[PyDataLens GitHub Issues](https://github.com/yourusername/PyDataLens/issues)

Enjoy using **PyDataLens** for your data analysis needs! 🚀
