#include <iostream>

void logNewError(const char * message, const char * tags="error") {
  std::cout << "message: " << message << std::endl;
  std::cout << "tags: " << tags << std::endl;
}