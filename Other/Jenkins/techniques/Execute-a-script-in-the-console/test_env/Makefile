.PHONY: build img

IMGNAME := test_jenkins_script

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start:
	docker run --rm -it -p 8080:8080 -p 50000:50000 $(IMGNAME)

background:
	docker run --rm -d -p 8080:8080 -p 50000:50000 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')