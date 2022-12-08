#!/bin/bash
# Triggers a test run against the main version of Wagtail

# This job will is scheduled in the config.yml, this script is here to help test the job

curl -u ${CIRCLE_API_USER_TOKEN}: \
     -d build_parameters[CIRCLE_JOB]=nightly-wagtail-test \
     https://circleci.com/api/v1.1/project/github/allcaps/wagtail-font-awesome-svg/tree/main
