from setuptools import setup, find_packages


setup(
name="log-analyzer-basic",
version="0.1.0",
description="Basic Log Analyzer with anomaly detection (regex + pandas)",
author="Your Name",
packages=find_packages(where="src"),
package_dir={"": "src"},
install_requires=[
"pandas>=2.2",
"PyYAML>=6.0",
"Jinja2>=3.1",
"matplotlib>=3.8",
"python-dateutil>=2.9",
"rich>=13.7",
],
entry_points={
"console_scripts": [
"loganalyzer=main:run_cli",
]
},
python_requires=">=3.9",
)