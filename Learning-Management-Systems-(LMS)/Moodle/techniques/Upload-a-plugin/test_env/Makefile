.PHONY: build img

IMGNAME := awesome_rce_moodle

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start: build
	docker run --rm -it -p 10080:80 -p 13306:3306 $(IMGNAME)

background:
	docker run --rm -d -p 10080:80 -p 13306:3306 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')