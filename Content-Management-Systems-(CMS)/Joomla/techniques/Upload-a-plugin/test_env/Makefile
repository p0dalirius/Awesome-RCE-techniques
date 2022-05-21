.PHONY: build img

IMGNAME := awesome_rce_joomla

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start: build
	docker run --rm -it -p 8080:8080 $(IMGNAME)

background:
	docker run --rm -d -p 8080:8080 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')