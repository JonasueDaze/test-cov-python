# Test / Code Coverage in Python

A repository for testing Test Coverage / Code Coverage frameworks,
tools and libraries in Python

## Integrated tools

- [Codacy](https://app.codacy.com/gh/jonasue20/test-cov-python/dashboard)
  [![Codacy Badge](https://app.codacy.com/project/badge/Grade/13d894eeaade4d388b885d094426d225)](https://app.codacy.com/gh/jonasue20/test-cov-python/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
  [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/13d894eeaade4d388b885d094426d225)](https://app.codacy.com/gh/jonasue20/test-cov-python/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

- [CodeCov](https://app.codecov.io/gh/jonasue20/test-cov-python)
  [![codecov](https://codecov.io/gh/jonasue20/test-cov-python/branch/main/graph/badge.svg?token=EQZNSQMPZ0)](https://codecov.io/gh/jonasue20/test-cov-python)

- [Coveralls](https://coveralls.io/github/jonasue20/test-cov-python)
  [![Coverage Status](https://coveralls.io/repos/github/jonasue20/test-cov-python/badge.svg)](https://coveralls.io/github/jonasue20/test-cov-python)

## Setup instructions

The following tools are required:

- [Python 3](https://www.python.org/) (preferably with a virtual environment
  manager like [pyenv](https://github.com/pyenv/pyenv));
- [dbmate](https://github.com/amacneil/dbmate) and
  [PostgreSQL client binaries](https://www.postgresql.org/) for database migration;
- [Docker](https://docs.docker.com/) (preferably with Docker
  Compose v2) to spin up services;
- [Chrome](https://www.google.com/chrome/) for executing tests
  (which uses [Selenium](https://www.selenium.dev/))

To setup and execute the project's tests, execute these steps:

1. Spin up the project's services;

   ```shell
   docker compose up -d
   ```

2. After PostgreSQL is healthy, execute database migration;

   ```shell
   dbmate migrate
   ```

3. Install project's dependencies;

   ```shell
   pip install -r requirements.txt
   ```

4. Execute the tests;

   ```shell
   pytest --cov=. test
   ```
