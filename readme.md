# Hotel Reservation System

This project is a Hotel Reservation System built with Django. It allows users to browse available hotels, view room details, and make reservations. The web application is designed to be user-friendly and responsive, making it easy to navigate and book a hotel room on any device.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Browse available hotels
- Filter hotels by location and availability
- Secure user registration and login
- Make and manage reservations
- Admin panel for managing hotels, rooms, and reservations
- Responsive design for mobile and desktop devices

## Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- A virtual environment (recommended)

### Clone the Repository

```
git clone https://github.com/Razwanul-Islam/room-lagbe.git
cd room-lagbe
```

### Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # for Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Now, apply the migrations to create the necessary tables.

```bash
python manage.py migrate
```

### Create a Superuser

Create a superuser to access the admin panel.

```bash
python manage.py createsuperuser
```

### Running the Development Server

Start the development server on your local machine.

```bash
python manage.py runserver
```

Now you can access the web application at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

- Browse the available hotels and filter them according to your preferences.
- Register for an account and log in to make reservations.
- Log in as a hotel manager to manage hotels, rooms, and reservations in the admin panel.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.