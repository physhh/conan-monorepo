#include <world/a.h>

#include <hello/a.h>
#include <iostream>

namespace world {

void do_a() {
  hello::do_a();
  std::cout << "Doing 'a'..." << std::endl;
}

} // namespace world