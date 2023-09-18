# Chess Video Renderer
 Convert Video Into Chess Boards 

Here are some basic instructions on how to convert a video:  
1) Create "frames" and "out" folders 

2) Add video frames to "frames" folder 

	This can be done a plethora of ways but if you're unsure how, I would personally use FFMPEG (A few sample commands are in the "ffmpeg.txt" file) 
	Ensure frames have a [frame%4d] naming scheme (ffmpeg makes this very easy) 
	Ensure frames have a standard resolution. (I've had weird issues with nonstandard sizes) 

3) In the chess_renderer.py file change the resolution and multiplier to your liking 

	Resolution: The resolution of the output frames. Ensure these have the same ratio as the input frames 
	Multiplier: Changes the number of pieces used to fill the screen. Play around with this number to get desired results 

4) Run chess_renderer.py 

	Ensure you run this from the same directory or else it won't see the files 

5) Convert generated frames to video 

	Similar to step 1, I would use ffmpeg but whatever gets the job done 
