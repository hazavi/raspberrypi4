all: create_folder copy_script run_script delete_folder delete_service restore_service

create_folder:
	# Create a temporary folder
	mkdir -p Temp

copy_script:
	# Copy the binary_clock.py script to the Temp folder
	cp /home/haz/senseHat/src/binary_clock.py Temp/

run_script:
	# Run the binary_clock.py script
	python3 Temp/binary_clock.py

delete_folder:
	# Delete the Temp folder
	rm -rf Temp

delete_service:
	# Stop and remove the binaryClock service
	sudo systemctl stop binaryClock.service
	sudo systemctl disable binaryClock.service
	sudo rm /etc/systemd/system/binaryClock.service
	sudo systemctl daemon-reload

restore_service:
	# Restore the binaryClock service
	sudo cp binaryClock.service /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl enable binaryClock.service
	sudo systemctl start binaryClock.service