// g++ -Dcimg_display=0 -Dcimg_use_png=1 -I CImg -Wall -Wextra -o hexdragon hexdragon.cpp -lpng -lz

#include "CImg.h"
#include <cmath>
#include <complex>
#include <iostream>
#include <vector>

using namespace cimg_library; 

int main(void)
{
  const int width = 1600;
  const int height = 900;
  CImg<unsigned char> img(width, height, 1, 3, 255); // White background

  const int r = 5;
  const int step = 10;
  std::vector<std::complex<double>> c;
  c.push_back(std::complex<double>(120, 300));
  c.push_back(std::complex<double>(120, 300 - step));

  for (int i = 0; i < 9; i++) {
    int last_index = c.size() - 1;
    for (int j = last_index - 1; j >= 0; j--) {
      auto z = c[j] - c[last_index];
      const double phi = 2 * cimg::PI / 3;
      auto new_pos = std::polar(std::abs(z), std::arg(z) + phi) + c[last_index];
      c.push_back(new_pos);
    }
  }

  int count = 0;
  for (auto it = c.begin(); it != c.end(); it++) {
    // Calculate hexagon vertices
    int px[6], py[6];
    for (int i = 0; i < 6; ++i) {
      px[i] = static_cast<int>(it->real() + r * std::cos(cimg::PI * i / 3));
      py[i] = static_cast<int>(it->imag() + r * std::sin(cimg::PI * i / 3));
    }

    // Fill the hexagon by drawing 6 triangles from the center
    const unsigned char black[] = {0, 0, 0};
    for (int i = 0; i < 6; ++i) {
      int j = (i + 1) % 6;
      img.draw_triangle(it->real(), it->imag(), px[i], py[i], px[j], py[j], black);
    }

    count++;
  }
  std::cout << count << " hexagons total" << std::endl;

  img.save_png("hexdragon.png");
  return 0;
}
