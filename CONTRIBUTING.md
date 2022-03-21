# Contributing

Thank you for contributing to this repo!

Helpful links:
- [Slack notifications](#slack)
- [Branching](#branching)
- [Setup](#setup)
- [Testing](#testing)
- [Deploys](#deploys)


## Slack
This repo will post a PR and tag reviews in **YOUR SLACK CHANNEL HERE**.
To add yourself to this:
1. Grab your slack id (go to your profile, select the more option, copy member id)
1. Update the [slackNotify.yml](.github/workflows/slackNotify.yml) with your information in `slackUsers`.
```json
{ "github_username": "your-gh-user-name", "slack_id": "from-step-1" }
``` 

## Branching

| Property | Value     | 
| :-------- | :------- | 
| branch from      | main |
| naming convention | brief-branch-description/sc-number 

It is recommended you use the git helpers in shortcut.
For example:

`create-repo/sc-218494`

## Setup

<!---
 Fill in how to get your project up and running 
 Maybe something like:
 pip install --upgrade pip
 make install
 make build
--->

## Testing

All tests run on every commit and must pass before merging to `main`. 

<!---
 Fill in how to run integration and unit tests locally
 Maybe something like:
 make test-unit
 make test-integration
--->

## Deploys

<!---
 Fill in how your code is deployed
 Is it in github actions, is it in circle
--->

### Custom Metrics
Datadog no longer supports forwarding from cloudformation logs for custom metrics.

In order for metrics to get forwarded to datadog from a lambda:
1. Deploy the lambda
1. Run the following
```bash
export DATADOG_API_KEY="<DD_API_KEY>"
export DATADOG_SITE="<DD_SITE>"
export AWS_ACCESS_KEY_ID="<ACCESS KEY ID>"
export AWS_SECRET_ACCESS_KEY="<ACCESS KEY>"

npm install -g @datadog/datadog-ci
datadog-ci lambda instrument -f your-lambda-function-name-here -r region -v version -e extension-version
``` 

For more information see: [datadog serverless forwarder](https://docs.datadoghq.com/serverless/installation/python/?tab=datadogcli)