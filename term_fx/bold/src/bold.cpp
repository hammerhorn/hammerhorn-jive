#include <iostream>
#include <string>

// Appends one newline no matter what.
int main(int argc, char* argv[])
{
  std::string text;
  std::getline(std::cin, text);
  //std::cin.getline(text, 80);
  std::cout << "\033[1m" << text << "\033[0m" << std::endl;

  return 0;
}
 
