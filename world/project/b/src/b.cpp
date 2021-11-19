#include <world/b.h>

#include <hello/b.h>
#include <iostream>

namespace world {

void do_b() {
  hello::do_b();
  std::cout << "Doing 'b'..." << std::endl;
}

} // namespace world