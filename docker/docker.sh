case "$1" in
	build)
		sudo docker build --force-rm -t $2 . -f docker/$2/Dockerfile
		;;
	run)
		sudo docker run -ti -e DISPLAY=$DISPLAY -v $(pwd):/mnt/Prism -v /tmp/.X11-unix/:/tmp/.X11-unix/ -p 2222:22 $2
		;;
esac
