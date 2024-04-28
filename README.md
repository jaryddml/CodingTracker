# Window Activity Tracker
Introduction

The Window Activity Tracker is a powerful Python application designed to monitor and log the duration of active windows in a user's graphical environment, specifically targeting development environments like Visual Studio Code. This tool is particularly useful for developers and analysts who want to track time spent on different projects or files, offering insights that can help optimize productivity and project planning.

Built using Python and the EWMH (Extended Window Manager Hints) library, this application taps into the X Window System to fetch active window data, making it suitable only for Linux systems with X11. The project leverages SQLite for local data storage, ensuring all activity data is stored efficiently and can be queried for reporting and analysis purposes.
Key Features

    Activity Tracking: Monitors active windows and logs duration spent on each window that matches specified criteria (e.g., windows titled "Visual Studio Code").
    Data Persistence: Utilizes SQLite database to store activity logs, providing robust data handling and easy retrieval.
    Real-time Monitoring: Runs in the background, updating the activity database in real-time as window focus changes.
    Extensibility: Easily extendable to support more editors or development environments beyond Visual Studio Code.

Installation
Prerequisites

    Linux OS with X11 display server
    Python 3.6 or higher
    SQLite3

Setup Environment

Clone the repository and set up a Python virtual environment:
    git clone https://github.com/jaryddml/CodingTracker.git
    cd window-activity-tracker
    python -m venv venv
    source venv/bin/activate

Install Dependencies

Install the required Python packages:
    pip install -r requirements.txt

Usage

To start the activity tracker, run the main script:
    python project.py

This will initiate the tracking service, which will run silently in the background. To view the activity logs, you can start the gui:
    python gui.py

The gui gets the data from the database and displays your individual files with the total amount of time spent in each one.
Using sqlite and using minimal minumal recourses this is a very lightweight program that you will not notice.
I Have been running it with no crashes and no adverse effects. 
