# Video Textures

## Synopsis

In this assignment we will be applying our Computational Photography magic to video, with the purpose of creating [video textures](http://www.cc.gatech.edu/cpl/projects/videotexture/) (infinitely looping pieces of video). These are basically gifs with very smooth transitions, as seen in the lectures, and the process is described in the Scholdl, et al. paper *Video Textures*. You are required to take your own input video in order to generate a smooth original video texture.

To help you with this assignment, you should carefully read the required technical paper, and watch the associated modules:
   - ["Video Textures"](https://dl.acm.org/doi/10.1145/344779.345012) (Schödl, A.,  Szeliski, R., Salesin, D., & Essa, I.)
   - Module 06-01: Video Processing
   - Module 06-02: Video Textures
   - Module 06-03: Video Stabilization


## Instructions

### 1. Implement the functions in the `textures.py` file.

- `videoVolume`: Take a list containing image numpy arrays, and turn them into a single array which contains the entire video volume.
- `computeSimilarityMetric`: Find the "distance" between every pair of frames in the video.
- `transitionDifference`: Incorporate frame transition dynamics into a difference matrix created by computeSimilarityMetric.
- `findBiggestLoop`: Find an optimal loop for the video texture. (NOTE: part of your task is to determine the best value for the alpha parameter.)
- `synthesizeLoop`: Take our video volume and turn it back into a series of images, keeping only the frames in the loop you found. 

The docstrings of each function contains detailed instructions. You may only have a limited number of submissions for each project, so you are *strongly* encouraged to write your own unit tests. **Do *NOT* try to use the autograder as your test suite.** The `test_textures.py` file is provided to get you started. Your code will be evaluated on input and output type (e.g., uint8, float, etc.), array shape, and values. Be careful regarding arithmetic overflow!

When you are ready to submit your code, you can submit it to the Gradescope autograder for scoring, but we will enforce the following penalty for the submissions:

- <= 10 submissions -> No penalty 
- <= 20 but >10 submissions -> -5 penalty
- <= 30 but >20 submissions -> -10 penalty
- more than 30 submissions -> -20 penalty

**Notes:**
- Downsampling your images will save processing time during development. Larger images take longer to process, and may cause problems for the VM and autograder which are resource-limited.

- The `main.py` script reads files in the sorted order of their file name according to the conventions of python string sorting; it is essential that file names are chosen so that they are in sequential order or your results will be wrong. 

### 2. Use these functions on the sample (candle) images to make a video texture

Use the images in the `videos/source/candle` directory to create a smooth video texture. We provided these images for testing -- _do not include these images in your resources submission_ (although the output should appear in your report). Refer to Section 4 below on finding a good alpha.

### 3. Use these functions on your own input images to make a video texture - _READ CAREFULLY_

For this section of the assignment, **you are required to take your own input video and extract the image frames to generate your own video texture result. Do NOT use video clips from the web**. Refer to Section 4 below on finding a good alpha.

See the appendix, “Working with Video”, for instructions to extract image frames from video clips, and tips on converting the image frames back to a video gif. Host your video gif & input frames on GT Box. Provide a working sharing link in your report so that anyone with the link may view the video gif. 

**IMPORTANT REMINDER:** You are responsible to ensure that links to your GIFs in your report function properly. _We will not accept regrade requests if your images are missing because the links are expired or unviewable._

### 4. Finding a good alpha
The last bit of computation is the alpha parameter, which is a scaling factor. The size of the loop and the transition cost are likely to be in very different units, so we introduce a new parameter to make them comparable. We can manipulate alpha to control the tradeoff between loop size and smoothness. Large alphas prefer large loop sizes, and small alphas bias towards short loop sizes. You are looking for an alpha between these extremes (the goldilocks alpha). Your findBiggestLoop function has to compute this score for every choice of start and end, and return the start and end frame numbers that corresponds to the largest score. 

You must experiment with alpha to generate a loop of reasonable length (and that looks good) - more than one frame, and less than all of the frames. Alpha may vary significantly (by orders of magnitude) for different input videos.  When your coding is complete, the `main.py` program will generate visualization images of the three difference matrices: similarity, transition, and scoring.  These matrices may help you identify good alpha values.

**IMPORTANT REMINDER: Discussing the alpha values you experimented with before deciding on the best alpha value for each video texture (candle and your own) is required in your report. Make note of the values while you experiment and how they affect your results. Please read through the provided template for more information before starting on the assignment.** 

### 5. Complete and Submit the Report on Gradescope AND Canvas

- The total size of your report+resources must be less than **20MB** for this project. If your submission is too large, you can reduce the scale of your images or report. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf) or other apps.

Download a copy of the A5 report template provided in this directory and answer all of the questions. You may add additional slides to your report if necessary. Save your report as `report.pdf`. Submit your PDF to **A5-Video Textures Report** on Gradescope. 

Remember that in the report template, you are asked to provide a link to a directory that contains:
1. Your final candle video texture gif
2. Your original video
3. Your final original video texture gif
4. A folder that has all of the frames from your original video (no need to include a folder of frames for the sample candle)

**Do NOT submit these in resources.zip. Providing a working link in your report is a strict requirement.**

After you upload your PDF, you will be taken to the "Assign Questions and Pages" section that has a Question Outline on the left hand side. These outline items are determined by the Instructors. **For each question - select the question, and then select ALL pages that go with that question. This is important to do correctly because any pages that are not selected for the corresponding question might get missed during grading.**

In order for your report to be uploaded to the Peer Feedback system, submit your PDF on **Canvas > Assignments > A5:Video Textures Report**. This is required. 


### 6. Submit the Code on Gradescope

Create an archive named `resources.zip` containing your `textures.py` file. Submit your `resources.zip` to **A5-Video Texture Resources** in Gradescope for grading.

You are required to submit only your code in resources.zip. All of the other required resources for this assignment must be hosted online and working links must be provided in your report (see Section 5 above). 

Once you’re finished with submitting this assignment, give yourself a pat on the back (or a hug!) because you’re done with the homework assignments for this course!

**Notes:** 

   - **EXIF metadata:** When including or sharing images, make sure there are no data contained in the EXIF metadata that you do not want shared (i.e. GPS). If there is, make sure you strip it out before submitting your work or sharing your photos with others. Normally, we require that your images include aperture, shutter speed, and ISO. You may use `pypi/exif` library in a separate python file to strip GPS data if you wish.  Make sure you do not use an app that strips all exif from the image. 

  - **DO NOT USE 7zip.** We've had problems in the past with 7z archives, so please don't use them unless you don't mind getting a zero on the assignment.
  
  - **Note for Mac users:** If you zip your files, do it from within the folder by selecting the files.  Do not zip the directory.  What happens is that the Mac adds extra stuff and that might confuse Gradescope.


## Criteria for Evaluation

Your submission will be graded based on:

  - Correctness of required code
  - Creativity & overall quality of results
  - Completeness and quality of report


## Appendix - Working with Video

Working with video is not always user friendly. It is difficult to guarantee that a particular video codec will work across all systems. In order to avoid such issues, the inputs for this assignment are given as a sequence of numbered images.

You may use tools such as Gimp and others to break your own video into separate image frames. Alternatively, there are tools discussed below that you can use to split your own videos into frames, and to reassemble them into videos. These programs may not work for everyone depending on your operating system, software versions, etc. You will need to find something that works for you, so you can produce your results as a gif! Googling for image->gif tools online and asking other students on Piazza may help.

**ffmpeg (avconv)**
These are free and very widely used software for dealing with video and audio.

- ffmpeg is available [here](http://www.ffmpeg.org/)
- avconv is available [here](https://libav.org/avconv.html)

Example ffmpeg Usage:

You can use this command to split your video into frames:
```ffmpeg -i video.ext -r 1 -f image2 image_directory/%04d.png```

And this command to put them back together:
```ffmpeg -i image_directory/%04d.png out_video.gif```
