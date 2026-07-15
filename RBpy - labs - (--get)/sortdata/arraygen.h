#pragma once
#include <random>
namespace arrgen {
    void generate_random_array(int* array, int length, unsigned int seed) {
        std::mt19937 gen(seed);
        std::uniform_int_distribution<> dis(1, 100); 

        for (int i = 0; i < length; ++i) {
            array[i] = dis(gen);
        }
    }
    void generate_increasing_array(int* array, int length) {

        for (int i = 0; i < length; ++i) {
            array[i] = i+1;
        }
    }
    void generate_decreasing_array(int* array, int length) {
        for (int i = 0; i < length; ++i) {
            array[i] = length-i;
        }
    }
}