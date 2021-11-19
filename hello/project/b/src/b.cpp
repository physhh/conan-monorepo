#include <hello/b.h>

#include <iostream>

namespace hello {

void do_b() {
  fmt::print("lal {}", 21 + 21);
  std::cout << "Doing 'b'..." << std::endl;
}

} // namespace hello