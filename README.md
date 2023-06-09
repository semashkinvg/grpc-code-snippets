[![Build Docker Image of Python Server](https://github.com/semashkinvg/grpc-code-snippets/actions/workflows/docker-image-python-server.yml/badge.svg?branch=main)](https://github.com/semashkinvg/grpc-code-snippets/actions/workflows/docker-image-python-server.yml)

# Summary

I want to make gRPC services in different programming languages to have those code snippets handy. On top of that, I plan to package those services in containers and deploy them to Minikube, so I have noted how to do that. To complete the dev cycle, I'm inclined to build a robust CI pipeline on GitHub actions and CD using ArgoCD to my Minikube.

## How to make a python app

from the root repostiory folder:
```bash
chmod +x ./protos/generate.sh
./protos/generate.sh ./src/python/client
./protos/generate.sh ./src/python/server
```
run apps in debug

## Minikube
A long with have codes to create gRPC services on many languages I build them and deploy to K8S (minikube) in my case

### Issue: Couldn't pull image from ghcr.io
apparently `minikube start` did work very well to me as I spent dissent amount of time authenticating to `ghcr.io` using guides like [this](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/). All of a sudden, seems like the issue was in the network, not in the auth. [simple trick](https://github.com/kubernetes/minikube/issues/8902#issuecomment-697834355) helped me a lot.
