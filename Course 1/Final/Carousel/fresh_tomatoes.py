import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="UTF-8">

  <title>Fresh Tomatoes!</title>

  <link href="bootstrap.min.css" media="screen" rel="stylesheet" type="text/css" />
  <link href="style.css" media="screen" rel="stylesheet" type="text/css" />

  <script src="jquery-1.11.2.js" type="text/javascript"></script>
  <script src="bootstrap.min.js" type="text/javascript"></script>
  <script src="carousel.js" type="text/javascript"></script>
  <script src="movies-modal.js" type="text/javascript"></script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>
<!-- Trailer Video Modal -->
  <div class="modal" id="trailer">
    <div class="modal-dialog">
      <div class="modal-content">
        <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
          <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
        </a>
        <div class="scale-media" id="trailer-video-container">
        </div>
      </div>
    </div>
  </div>

<div class="container-fluid">
<div class="row-fluid">
<div class="span12">

    <div class="page-header">
        <h3>Fresh Tomatoes! Movie Trailers</h3>
        <p>Some of my Favorite Movies</p>
    </div>
        
    <div class="carousel slide" id="myCarousel">
        <div class="carousel-inner">
            <div class="item active">
                    <ul class="thumbnails">
                        {movie_tiles}
                    </ul>
              </div><!-- /Slide3 --> 
        </div>

        <div class="control-box">                            
            <a data-slide="prev" href="#myCarousel" class="carousel-control left"><</a>
            <a data-slide="next" href="#myCarousel" class="carousel-control right">></a>
        </div><!-- /.control-box -->

    </div><!-- /#myCarousel -->
        
</div><!-- /.span12 -->          
</div><!-- /.row --> 
</div><!-- /.container -->

</body>

</html>
'''

# A single movie entry html template
movie_tile_content = '''

<li class="span3">
      <div class="thumbnail movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
          <a href="#"><img src="{poster_image_url}" alt=""></a>
      </div>
      <div class="caption">
          <h4>{movie_title}</h4>
  <p>Nullam Condimentum Nibh Etiam Sem</p>
          <a class="btn btn-mini" href="#">-- Read More</a>
      </div>
</li>

'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
