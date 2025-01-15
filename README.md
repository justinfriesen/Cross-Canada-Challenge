# CrossCanadaChallenge

A Flask web application built to support the UW WELL-FIT program's 20th anniversary fundraising initiative. The app transforms a spreadsheet-based fitness tracking system into an interactive map-based journey across Canada, designed specifically for cancer, stroke, and dementia patients participating in the WELL-FIT program.

![CrossCanadaChallenge App Interface](path-to-your-image.png)

## Project Overview

This application was developed during a co-op term at the University of Waterloo's Centre for Community, Clinical and Applied Research Excellence (CCCARE). It visualizes participants' exercise progress as a virtual journey across Canada, with 16 major landmarks serving as milestones.

### Features

- Interactive Google Maps visualization of team progress
- User authentication with role-based access control
- Real-time progress tracking and updates
- Automated milestone achievements
- Team comparison capabilities
- Distance conversion from exercise activities to travel distance

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **APIs**: Google Maps JavaScript API
- **Authentication**: Flask-Login

## Project Structure

```
website/
├── __pycache__/
├── static/
├── templates/
├── __init__.py
├── auth.py
├── database.db
├── helpers.py
├── models.py
└── views.py
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/justinfriesen/Cross-Canada-Challenge.git
cd Cross-Canada-Challenge
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Flask and required dependencies:
```bash
pip install flask flask-login # Add any other dependencies
```

4. Set up your Google Maps API key in the appropriate configuration file

5. Run the application:
```bash
python -m flask run
```

## Configuration

To run this application, you'll need:
- A Google Maps API key
- Python 3.7 or higher
- Flask and its dependencies (see requirements.txt)

## Contributing

This project was a learning exercise and is no longer actively maintained. However, feel free to fork it and adapt it for your own needs.
