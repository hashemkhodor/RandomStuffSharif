#! /usr/bin/bash

read -p 'Enter database Name(No spaces):' database
if [  -z "$database" ] ; then
	echo "Empty String for database isn't accepted"
	exit 0
fi
read -p 'Which assignment to export?(Do not put spaces in the name):' assignment


if [ ! -z "$assignment" ] ; then
	read -p 'Enter any problem name:(Do not put spaces):' problem
	if [ ! -z "$problem" ]; then
		read -p 'Specify the export directory(by default /var/www/Submissions):' direc
		if [ -z "$direc" ];then
			direc="/var/www/Submissions" 
		fi
			#First get id of assignment and remove spaces
			id=$(sudo -u postgres -H -- psql -d $database -t -c "Select assignment from shj_problems where name like '%$problem%'" | tr -d ' ' )
			#Remove Spaces
	  		 
			#echo "id is: $id  " 
			if [ ! -z "$id" ] ; then

				sudo -u postgres -H -- psql -d $database -c "\copy ( SELECT username, pre_score, coefficient, assignment,problem FROM shj_submissions Where is_final=1 and assignment=$id order by username, problem) to '$direc/$assignment.csv' csv header;"

		
				Output=$(find $direc/$assignment.csv )
	
				if [ "$Output" = "$direc/$assignment.csv" ] ; then
					echo "Exporting grades to $direc/$assignment.csv was succesful";
				else
					echo "Exporting failed"
				fi
			else
				echo "Assignment not found"
			fi
	else
		echo "Empty problem not acceptable"
	fi

	

else 
	echo "Empty string not acceptable."
fi
