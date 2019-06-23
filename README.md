# user_collection
sample python code for interacting with data stored in different file types.

run application:
	user_collection:
		Display or convert User collection data.
		    display          Command to display file contents.
		    convert          Command to convert file contents to different file.

	user_collection  display:
			filepath              Path of file to parse and display.
			-fo FORMAT, --format FORMAT
			                        Format to display the file in, options: text, html.
		                        
	user_collection convert:
			source_filepath       Filepath to parse data from.
			destination_filepath  File path to store data to.
			

Example commands:
	user_collection display resources/xml_data.xml
	user_collection display resources/json_data.json --format html
	user_collection convert resources/json_data.json output/json_output_data.xml 
	user_collection convert resources/xml_data.xml output/xml_output_data.json 
	
Run unittests:
	./test
