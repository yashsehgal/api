#include "LogError.h"
#include "LogWarning.h"
#include "LogInfo.h"
#include "LogSuccess.h"
#include "LogMessage.h"
#include <iostream>

class LoggingActivity {
  private:
  const char *filename;
  const char *file_description;
  const char *method_name;
  const char *author_name;

  /// error type
  const char *error_type;
  public:

  LoggingActivity(const char * __filename="default", char * __file_description="description...", 
                  const char * __method_name="<UNKNOWN>", const char * __author_name="<UNKNOWN>") {
    filename = __filename;
    file_description = __file_description;
    method_name = __method_name;
    author_name = __author_name;
  }

  void setProperties(const char *__filename = "default", char *__file_description = "description...",
                     const char *__method_name = "<UNKNOWN>", const char *__author_name = "<UNKNOWN>") {
    filename = __filename;
    file_description = __file_description;
    method_name = __method_name;
    author_name = __author_name;
  }

  void showProperties(void) {
    std::cout << "filename> " << filename << std::endl;
    std::cout << "file-description" << file_description << std::endl;
    std::cout << "method-name" << method_name << std::endl;
    std::cout << "author-name" << author_name << std::endl;
  }
};