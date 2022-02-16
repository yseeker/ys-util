if [! docker images | grep ${IMAGE_NAME}]; then
    docker build ./docker -t ${IMAGE_NAME}
fi
if [! docker ps --format "{{.Names}}" | grep ${CONTAINER_NAME}]; then
    docker run
    else
    docker exec
fi