# Transportation_system

## How to run

To run Transportation System in development mode; Just use steps below:

1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/mmadreza99/transportation_system`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/mmadreza99/Transportation_system && cd transportation_system
  virtualenv -p python3 .venv  # Create virtualenv named venv
  source vene/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
  ```

4. Run `transportation_system` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your transportation system version.

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python3`, `pip`, `virtualenv` 
2. Clone the project using:  `git clone https://github.com/mmadreza99/transportation_system`.
3. Make Environment Ready Like This:
``` Command Prompt
cd transportation_system
python -m virutalenv .venv # Create virtualenv named .venv
.venv\Scripts\activate.bat # Activate The Virutal Environment
pip install -r requirements.txt
python manage.py migrate # Create Database Tables
```
4. Run `transportation_system` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Transportation System version.

