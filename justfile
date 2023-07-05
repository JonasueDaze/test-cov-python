set dotenv-load

test:
  pytest --cov=. --cov-report=xml test

scan: test
  sonar-scanner -Dsonar.token=$SONAR_TOKEN
