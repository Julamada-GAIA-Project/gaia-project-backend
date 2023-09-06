# GAIA Project Backend
GAIA Project API

## Docker Image
Environment vars required in run command to protect CosmoDB secrets

### Run cmd
  docker run -e COSMODB_URI=[uri] -e COSMODB_KEY=[key] -e COSMODB_NAME=[name] -e COSMODB_CONTAINER=[container] ghcr.io/julamada-gaia-project/gaia-project-backend:latest
  
