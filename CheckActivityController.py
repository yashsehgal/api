from typing import Dict
import LogError as LogError

class CheckActivityController:
  
  def __init__(self) -> None:
      super.__init__()
    
  def check_video_playlist_availability(self, video_url=None, video_tags=None):
    if video_url is not None and video_tags is not None:
      self.video_response_dmt = video_url + " " + video_tags
      if 'response' in self.video_response_dmt and 'not available in your country' in video_tags['response'][0]:
        self.error_response_logger = LogError(
          statement="""
          TITLE: Top 10 Video Editing Tricks in just 5 minutes
          DESCRIPTION: LIKE. SHARE AND SUBSCRIBE
          """, default=None)
        
  '''
  This method is written to check whether a video
  is available or not in the database. Is the video
  will not be able to fetched by the system, this method
  will take care of all the bug bursting at the backend 
  server. Also, It reduces time to fetch other related videos.
  '''
  
  def check_video_availability(self, video_url=None, video_tags=None):
    if video_url is not None and video_tags is not None:
      self.video_response_dmt = video_url + " " + video_tags
      if 'response' in self.video_response_dmt and 'not available in your country' in video_tags['response'][0]:
        self.error_response_logger = LogError(
          statement="""
          TITLE: Top 10 Video Editing Tricks in just 5 minutes
          DESCRIPTION: LIKE. SHARE AND SUBSCRIBE
          """, default=None)
        
  def check_video_thumbnail_quality(self, video_url=None, video_tags=None):
    self.video_thumbnail_image = self.retrieve_video_thumbnail(
      _video_url=video_url,
      _size_in_pixels="1800x720",
      _minimum_bit_rate=None)
    
    
  def retrieve_video_thumbnail(self, _video_url=None, _size_in_pixels=None, _minimum_bit_rate=None):
    self.video_url = _video_url
    self.size_in_pixels = _size_in_pixels
    self.minimum_bit_rate = _minimum_bit_rate
    
    FETCH_IMAGE_DMT_LIST = []
    IMAGE_PROPERTIES_DMT_LIST = []
    for image_count in range(len(self.number_of_videos)):
      FETCH_IMAGE_DMT_LIST.append(  
        FETCH_IMAGE_DMT = {
          "image_filename": self.set_image_filename("{}_VideoThumbnail.png".format(self.video_url)),
          "image_file_url": self.set_image_file_url("{}/:thumbnail:{}_VideoThumbnail.png".format(self.video_url, image_count)),
          "video_bit_rate": LogError.LogError.check_video_bit_rate(video_url=_video_url)
        }
      )
      
      IMAGE_PROPERTIES_DMT_LIST.append(  
        IMAGE_PROPERTIES_DMT = {
          "image_dmt": FETCH_IMAGE_DMT_LIST,
          "image_dmt_object": Dict(FETCH_IMAGE_DMT_LIST[0]),
          "type": type(FETCH_IMAGE_DMT_LIST[0])
        }
      )
