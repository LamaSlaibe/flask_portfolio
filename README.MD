## Flask Portfolio Website

A modern, dark-themed personal portfolio website built using Python and Flask .
It show cases technical skills,projects,Github repositories,and contact information
with a clean responsive card-based layout.

### Project Objectives

This project aims to:
* Build a dynamic and interactive web portfolio using Python and Flask.
* Implement a professional dark theme UI with custom card designs and Devicon technology icons.
* Practice web routing, template rendering, and assest management in Flask.
* Create a user-friendly and responsive developer showcase experience.

### Features

* Clean dark theme UI (`#0f172a` background with rounded styling)
* Dedicated sections for technical skills,Github repositories, and contact details
* Integration of official Devicon SVG icons for programming languages and tools
* Responsive design across multiple device screens
* Configured structural organization for templates and static assets

### Requirements

* Python 3 (verified with Python 3.12.0)
* Flask framework
* standard libraries with no extra external complex dependencies

### Installation

Flask package install is required.

```bat
pip install flask
python -m venv .venv
.venv\Scripts\activate
```

### How to run

From the folder that contains `app.py`:

```bat
python "app.py"
```

open your web browser and navigate to 
https://127.0.0.1:5000

### Project structure

```text
flask_portfolio/
├── static/ 
|     ├──css/
|     |   └──style.css
|     └──js/
|          └──script.js
├── templates/
    └──index.html
├── app.py
├── .gitignore             
└──README.md

### Example usage

```text
1. Start the flask server:
python app.py
2. Open your web browser and goto:
[https:/127.0.0.1:5000](https:/127.0.0.1:5000)
3. Navigate through the portfolio sections:
- Home/Welcome section
-Technicals Skills &Tools
-Featured Projects &Github Repositories
-Contact Information

Thanks for visiting! 👋
```

### How it Works

1. The Project initialization a Flask backend application using 'app.py.
2. Dynamic Html templates are rendered from the 'templates/' directory.
3. Static assests like css styles and javascripts scripts are served from the 'static/' directory.
4. Users can view technical skills, project showcases.

### What I Learned

Developing this portfolio helped solidify understanding of:

* Building Web applications using the 'Flask' micro-framework.
* Routing and rendering templates with Python and Html.
* Organization Project Structure Using 'Static/' and 'templates/' folders.
* Front-end styling and layout responsiveness for web interfaces.

### Project Purpose

This Portfolio Project serves as a:

* **Showcase:** Highlights technical skills, completed projects, and Github repositories.
* **Practical application:** Demonstrates core Web Development concepts using Python and Flask.

### Further Development

* Add a contact form with email notifiactions using Flask-Mail.
* Integrates a database (SQLite or MYSQL) to manage blog posts and portfolio items.
* Implement dark mode and nancd dynamic UI components.



