# {{ cookiecutter.project_slug }}

## Requirements

- make
- docker for mac
    - Please turn on `Enable Kubernetes` configulation if you want to deploy on local k8s
- flake8, pytest, mypy

## quick start

1. build docker image
```bash
make build-image
```

2. deploy on your local k8s cluster
```bash
make deploy
```

3. port-forward to k8s service resource
```bash
make port-forward
```

4. invoke health check endpoint
```bash
curl localhost:4600/health
{"msg":"I'm healthy"}
```

## test/lint/typecheck

```bash
make ci
```