# CI/CD Pipeline for simple Python Flask Service

Teaching app displaying name and message in different formats for the course of SBAT about
of Continuous Integration, Continuous Delivery and Continuous Deployment (DevOps).

### Technologies and platforms used:

1. [Python](https://www.python.org/) [[Flask](https://flask.palletsprojects.com/en/1.1.x/), [pytest](https://docs.pytest.org/en/stable/index.html)]
2. [Git](https://git-scm.com/)
3. [GitHub](https://github.com/)
4. [Travis-CI](https://travis-ci.com/)
5. [Docker](https://www.docker.com/)
6. [Docker-Hub](https://hub.docker.com/)


[] (# 7. [Heroku](https://www.heroku.com/) (Not needed for students))


### Python Web Service with Flask
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
  
  It should display something like:
  ```
  (base) user@pc:~/Projects/printerService$ python3 -m pytest -v test/
  ============================== test session starts ===========================================
  platform linux -- Python 3.8.3, pytest-6.2.1, py-1.9.0, pluggy-0.13.1
  rootdir: /home/Projects/printerService
  collected 7 items
  
  test/test_formater.py::Test_Formater::test_plain_uppercase PASSED                       [ 14%]
  test/test_formater.py::Test_Formater::test_plain_text PASSED                            [ 28%]
  test/test_formater.py::Test_Formater::test_get_formatted PASSED                         [ 42%]
  test/test_views.py::Test_Flask_Views::test_output PASSED                                [ 57%]
  test/test_views.py::Test_Flask_Views::test_outputs PASSED                               [ 71%]
  test/test_views.py::Test_Flask_Views::test_form PASSED                                  [ 85%]
  test/test_views.py::Test_Flask_Views::test_mult PASSED                                  [100%]
  ============================= 7 passed in 0.09s ==============================================
  ```
- By continuing to work with the project, activating and deactivating the hermetic environment for py application:

  ```
  # deactivation
  $ deactivate
  ```

  ```
  ...
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

- Docker Installation: [docker howto](https://docs.docker.com/engine/install/)

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
