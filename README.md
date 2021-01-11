# Simple Flask App

Teaching app displaying name and message in different formats for the course of SBAT about
of Continuous Integration, Continuous Delivery and Continuous Deployment (DevOps).

- <b>(Optional)</b> In the project, if you want you can use a virtual environment to create a hermetic environment for the application:

  ```
  # create a hermetic environment for application libraries:
  $ python3 -m venv .venv

  # activating the hermetic environment
  $ source .venv/bin/activate
  ```
  
- Independently if you use a virtual environment (in that case continue after the previous commands) or the base one, you can
  install the libraries in the following way:
  ```
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # see
  $ pip list
  ```

  Check out: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) and [flask library](http://flask.pocoo.org).

- Running the application:

  ```
  # as a regular program
  $ python main.py

  # or:
  $ PYTHONPATH=. FLASK_APP=app.py flask run
  ```

- Running tests (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  
  # or:
  $ python3 -m pytest -v test/
  ```

- By continuing to work with the project, activating the hermetic environment for py application:

  ```
  # deactivation
  $ deactivate
  ```

  ```
  ...

  # activation 
  $ source .venv/bin/activate
  ```

- Continuous Integration with TravisCI:

  ```
  # my notes about TravisCI
  ```
  
- Deployment with Docker:

  ```
  # my notes about docker
  ```

# Auxiliar Information

## Ubuntu

- Docker Installation: [docker howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Docker Installation:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
