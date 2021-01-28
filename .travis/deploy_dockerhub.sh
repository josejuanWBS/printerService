docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
TAG="latest"
else
TAG="$TRAVIS_BRANCH"
fi
slug=$TRAVIS_REPO_SLUG:$TAG
sl=$TRAVIS_REPO_SLUG
docker build -f Dockerfile -t "${slug,,}" .
docker tag "${sl,,}" $DOCKER_REPO
docker push $DOCKER_REPO
