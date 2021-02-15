class LogError:
  
  def __init__(self, statement=None, default=None) -> None:
    self.statement = statement
    self.default = default
    
  def check(self, errorname=None, errortag=None, 
              statement=None, default=None, accessID=None):
    if errorname is default:
      return True
    
  def set_video_playlist_url(self, video_url=None, video_refer_url=None):
    if video_url is not None and video_refer_url is not None:
      self.video_url = video_url
      self.video_refer_url = video_url
      
  def message(self, message_text=None):
    return message_text
  
  def check_video_bit_rate(self, video_url, video_rates=None):
    if video_url is not None and video_rates is not None:
      for rate_checker in video_rates:
        if video_rates[rate_checker][0] == 'NaN':
          return False
        
        if video_rates[rate_checker][1] == 'NaN':
          return False
        
        if video_rates[rate_checker][2] == 'NaN':
          return self.message(
            """
              This error rate list is empty
              The video playing rate record is not present in the list
              during the testing phase. Check the video bit rate computing
              algorithm again and test this feature again...
              
              The Rates are checked at 3 columns.
              ErrorType: ErrorCoded Method
            """
          )