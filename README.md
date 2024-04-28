
Window Activity Tracker

Welcome to the GitHub repository of the Window Activity Tracker! This tool is designed to help developers, analysts, and any professionals who spend considerable time on their computers, especially those using Linux systems, to monitor and log the duration of their active windows. Particularly beneficial for users of Visual Studio Code, this application extends its functionality to various other development environments by tracking active window durations to facilitate productivity analysis and project time management.
Project Background and Rationale

In today's fast-paced digital world, managing time efficiently is crucial, especially for developers and data analysts who juggle multiple projects. The idea for the Window Activity Tracker emerged from the need to quantitatively assess time spent on various projects without interrupting the flow of work. Built with Python and integrating the EWMH (Extended Window Manager Hints) library, this application utilizes the capabilities of the X Window System to fetch and log active window data, providing insights that are pivotal for enhancing productivity and optimizing project planning.

Why Python? The choice of Python for this project stems from its extensive library ecosystem and its robustness in handling backend operations like database interactions. Python's simplicity and readability make it a perfect fit for projects that involve real-time data processing and storage, such as this activity tracker.
Core Features

Activity Tracking: The primary feature of this tool is its ability to monitor and log the duration for which windows remain active. It's specifically fine-tuned to identify and record sessions from development environments like Visual Studio Code.

Data Persistence: Leveraging SQLite for local data storage ensures that all tracking data is stored securely and efficiently. SQLite provides a lightweight yet robust framework for local database solutions, which perfectly aligns with the need for a minimalistic yet effective storage mechanism for our tracker.

Real-time Monitoring: Running quietly in the background, the tracker updates the activity logs in real-time as the window focus changes. This feature allows users to maintain an uninterrupted workflow with the assurance that all data is being logged accurately.

Extensibility: While initially designed for Visual Studio Code, the architecture of the Window Activity Tracker allows for easy extensions to include other editors and development environments, demonstrating the application's versatile nature.

Installation
Prerequisites

Linux OS with X11 display server.
Python 3.6 or higher.
SQLite3.

Getting Started

Clone the repository and set up a Python virtual environment:

bash

git clone https://github.com/jaryddml/CodingTracker.git
cd window-activity-tracker
python -m venv venv
source venv/bin/activate

Install Dependencies

Install the necessary Python packages using:

bash

    pip install -r requirements.txt

Usage

To initiate the tracking service, run:

bash

    python project.py

This command starts the tracking service, which operates in the background. For viewing the logs and analyzing the data, launch the GUI with:

bash

    python gui.py



![gui](https://github.com/jaryddml/CodingTracker/assets/109385281/cc70bb6e-3923-4595-8abc-5db39fd50118)    

The GUI fetches data from the SQLite database and displays individual file records with the total amount of time spent, offering a user-friendly interface for data interaction.
Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull-up request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!
