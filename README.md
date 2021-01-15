

<h1 align="center">
  <br>
  <a href="#"><img src="Project\media\Images\Hocus Focus logo.png" alt="Markdownify" width="200"></a>
  <br>
Hocus-Focus
  <br>
</h1>

<p align="center">
  <a href="#"><img alt="GitHub issues" src="https://img.shields.io/badge/URL-website-blueviolet?logo=Python=for-the-badge" title="Live Demo"></a>
  </p>


## Project Description
All about the project

### Key Features   
* LivePreview - Make changes, See changes
  - Instantly see what your Markdown documents look like in HTML as you create them.
* Sync Scrolling
  - While you type, LivePreview will automatically scroll to the current location you're editing.
* GitHub Flavored Markdown  

## Resources  
1. Backend Framework: **Django** 
2. Front-end Framework: **Bootstrap**
3. Database used: **Sqlite**



## Installation

1. Fork and Clone
    <ol>
    <li>Fork Urja-SCL-maxo Repo</li>
    <li>Clone the repo to your local system.</li>
    </ol>

2. Create a Virtual Environment for the Project

    In Windows
    ```bash
    pip install virtualenv
    ```
    ```bash
    virtualenv -p python venv
    ```
    ```bash
    venv\Scripts\activate
    ```

    In Ubuntu/MacOS
    ```bash
    python -m virtualenv venv

    source venv/bin/activate
    ```

   If you are giving a different name other than `venv`, then please mention it in `.gitigonre` first

3. Install all the requirements

    ```bash
    pip install -r requirements.txt
    ```
## Development

4. Checkout to different branch
     ```git
    git status
    git pull
    git branch
    git checkout -b < your-branch-here >
    ```

5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run server
    ```bash
    python manage.py runserver
    ```

7. Do the changes and send a PR referencing the changes.

## Contributing/ Adding Features

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change in the project.