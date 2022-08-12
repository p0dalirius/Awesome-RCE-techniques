.PHONY: build img

IMGNAME := awesome_rce_rocketchat_add_integration

all : build start

build:
	docker build -t $(IMGNAME):latest -f Dockerfile .

start:
	docker run --rm -it -p 13000:3000 $(IMGNAME)

background:
	docker run --rm -d -p 13000:3000 $(IMGNAME)

shell:
	docker exec -it $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}') bash

stop:
	docker stop $(shell docker ps | grep $(IMGNAME) | awk '{split($$0,a," "); print a[1]}')