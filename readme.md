BYU Mechatronics API
====================

This is the 'backend' or API of the [BYU Mechatronics Frontend](https://github.com/plusk01/mechatronics-backend).

To setup and run on a Mac or Linux machine follow the following steps:

1. Setup your production environment
2. Installing your app
3. Setup a proxy to your app

### Setting Up a Production Environment ###

The following assumes Ubuntu 14.04, but should be relatively transferrable to other *nix based machines.

*See [Starting a Django 1.6 Project the Right Way](http://www.jeffknupp.com/blog/2013/12/18/starting-a-django-16-project-the-right-way/).*

1. Update your package manager and upgrade your machine.

    ```bash
    sudo apt-get update && sudo apt-get upgrade
    ```

2. Install `pip`, Python's package manager:

    ```bash
    sudo apt-get install python-pip
    ```

3. Install `virtualenvwrapper` to create virtual Python environments for your Python apps. This is good practice because different apps often require different dependency versions. This separates those concerns:

    ```bash
    pip install virtualenvwrapper
    ```

4. Add the following to your shell's startup (`.profile`, `.bashrc`, etc):

    ```bash
    export WORKON_HOME=/var/www/apps/.virtualenvs
    export PROJECT_HOME=/var/www/apps
    source /usr/local/bin/virtualenvwrapper.sh
    ```

5. Reload your startup file:

    ```bash
    source .profile
    ```

6. Install your database of choice. We will install `postgres`:

    ```bash
    sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev libncurses5-dev
    ```

### Installing App ###

1. Create an apps directory to house your app:

    ```bash
    mkdir ~/apps
    ```

2. Clone the repo onto the machine and `cd` into it:

    ```bash
    git clone https://github.com/plusk01/mechatronics-backend.git
    cd /var/www/apps/mechatronics-backend
    ```

3. Create a virtual environment for your app:

    ```bash
    mkvirtualenv mechatronics
    ```

4. Install app dependencies into your virtualenv:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `postgres` role:

    ```bash
    sudo -i -u postgres
    createuser --interactive # (don't allow super user or creating db)
    ```

6. Create a database:
    
    ```bash
    createdb your-database-name
    ```

7. Grant privileges to your user for the database:

    ```bash
    psql -c "GRANT ALL PRIVILEGES ON DATABASE your-database-name TO your-user-name"
    ```

8. Set a password for your user:

    ```bash
    psql -c "ALTER USER your-user-name WITH PASSWORD 'yourpassword';"
    ```

9. Copy the `mechatronics/local_settings.py.backup` to `mechatronics/local_settings.py` and make the `DATABASES` entry look like:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'your-database-name',
             'USER': 'your-user-name',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
         }
     }
     ```
10. With the virtualenv activated, run the following command inside of '/var/www/apps/mechatronics-backend/':

    ```bash
    python manage.py syncdb
    ```

    Follow instructions to create a superuser.

11. Set the `STATIC_ROOT` to the appropriate directory:

    ```python
    STATIC_ROOT = '/var/www/apps/mechatronics-static'
    ```

12. Collect all the static files with the following:

    ```bash
    python manage.py collectstatic
    ```

### Setting Up Nginx ###

1. Copy the `upstart` and `nginx` conf to the appropriate directories, and make a symlink for nginx:

    ```bash
    cp /var/www/apps/mechatronics-backend/conf/upstart-mechatronics.com /etc/init/mechatronics.conf
    cp /var/www/apps/mechatronics-backend/conf/nginx-mechatronics.conf /etc/nginx/sites-available/mechatronics.conf
    ln /etc/nginx/sites-available/api.mechatronics.conf /etc/nginx/sites-enabled/api.mechatronics.conf
    ```

2. Restart nginx:

    ```bash
    service nginx restart
    start mechatronics
    ```

-----------------------------

```bash
# Switch from systemd to upstart
sudo apt-get install upstart-sysv
sudo update-initramfs -u
sudo reboot

# Switch from upstart to systemd
sudo apt-get install ubuntu-standard systemd-sysv
sudo update-initramfs -u
sudo reboot
```

----------------------------

## Change log

**9 Sept 2018**
- Changed email address for contact form
