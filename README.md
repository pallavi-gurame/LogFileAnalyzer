# LogFileAnalyzer
The LogFileAnalyzer is a Python-based application designed to analyze log files and detect suspicious activities such as unauthorized access, failed logins, privilege escalation, phishing attempts, file tampering, and potential security breaches.
This tool works across Windows, macOS, and Linux and provides a clear report with graphical visualizations for better interpretation of log data.

# Features

Analyze Windows Security logs for suspicious activities
Detect failed login attempts, explicit credential usage, and privilege escalation
Generate a summary report in text and CSV formats
Provide graphical visualization of detected issues (bar charts, histograms, pie charts)
Allow users to extend detection patterns and remedies

# Requirements

Python 3.x
Use a virtual environment
Required Python Libraries
pandas
matplotlib
numpy
seaborn

# Installation

# Clone the repository

git clone https://github.com/your-username/LogFileAnalyzer.git
cd LogFileAnalyzer

# For macOS and Linux

1) Ensure Python 3.x is installed. If not, install it:

2) sudo apt-get install python3 python3-pip             # Debian-based

3) sudo pacman -S python python-pip                     # Arch-based

3) brew install python                                 # macOS (Homebrew)


4)Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

# For Windows

Ensure Python 3.x is installed from the official website

# Create a virtual environment:

python -m venv venv
venv\Scripts\activate

# Usage

Run the analyzer
python scripts/analyzer.py


# Output

A CSV file with analyzed logs
A text report with suspicious event summary
Visual charts (bar, pie, histogram) saved as images

# Example

After selecting a log file and running the analysis, you will see:
Detected suspicious activities
Recommended actions
A bar graph showing the top event IDs
<img width="514" height="445" alt="image" src="https://github.com/user-attachments/assets/95eb5aff-c7e0-45e5-9b24-25538930762a" />






<img width="445" height="425" alt="image" src="https://github.com/user-attachments/assets/ae735a18-0d1f-45d1-897c-0c3ccf0a6306" />


# Future Enhancements

🔹 Real-time monitoring of log files

🔹 Custom patterns and detection rules

🔹 SIEM integration for advanced detection and incident response
