# build
# docker build -t spidy .

docker run -it -v $PWD:/src/app spidy

# docker system prune -f

# TODO: auto stop crawler when reaching max links for dev usage (done)
# TODO: zip file path (done)

# TODO: resume from crawler_todo.txt
# TODO: crawl link only


#docker run -d -v $PWD:/data 501ce1923209

# start at 10:40