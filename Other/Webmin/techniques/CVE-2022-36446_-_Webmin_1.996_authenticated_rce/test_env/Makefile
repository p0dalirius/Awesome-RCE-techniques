.PHONY: build img

IMGNAME := awesome_rce_webmin_1_996
PORT := 10080

all : build

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start: build
	docker run --rm -it -p $(PORT):10000 $(IMGNAME)

background:
	docker run --rm -d -p $(PORT):10000 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')
