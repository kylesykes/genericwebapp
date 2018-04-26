# genericwebapp

[![CircleCI](https://circleci.com/gh/kylesykes/genericwebapp.svg?style=svg)](https://circleci.com/gh/kylesykes/genericwebapp)

[Dockerhub Image](https://hub.docker.com/r/kylesykes/genericwebapp/)

A generic flask app for learning purposes.  Learning and experimenting with Flask, Docker, CircleCI, and distroless images.

This sets up a simple flask server with gunicorn.  It does nothing but return a simple JSON response to the use when hitting the `/` or `/status` routes.  The helm chart is functional and deploys a pod to a kubernetes cluster which will serve up the requests if the ingress is properly configured.  If you deploy this locally, you can use `kubectl port-forward <pod_name> 8080:8080` to test the service yourself.

While basic, this helm chart has proven to be a useful starting point when building a new helm chart for a variety of purposes (web server or not).
