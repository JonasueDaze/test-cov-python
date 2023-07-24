set dotenv-load
set fallback

version := "3.10.9"
project := "pgc-" + version

test:
  pytest -s --cov=. --cov-report=html --cov-report=xml --cov-report=term --ignore=test/test_unittest.py

scan: test
  sonar-scanner -Dsonar.token=$SONAR_TOKEN

pyenv:
  pyenv install --skip-existing {{version}}
  if [ ! -d "$(pyenv root)/versions/{{project}}" ]; then \
    pyenv virtualenv {{version}} {{project}}; \
  fi
  pyenv pyright {{project}}
