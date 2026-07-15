#include <string>
#include <iostream>
#include <chrono>
#include <fstream>
#include "arraygen.h"
#include "sortfunc.h"
using namespace std;
using namespace sortsamples;
using namespace arrgen;
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
const int RANDSEED = 42;
const long long MAXMIN = 60;
const int RANGE = 10000000;
const int STEP = 100;
const string MAINDIR = "C:\\TEMP\\sortdata";
typedef void (*SortFunc)(int*, int);
SortFunc* init() { SortFunc res[] = { bubble_sort, insertion_sort,comb_sort,selection_sort, quick_sort,merge_sort, heap_sort, bubble_sort }; return res; }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
long long execute_func(SortFunc f, int* arr, int n) {
	auto start = chrono::high_resolution_clock::now();
	f(arr, n);
	auto end = chrono::high_resolution_clock::now();
	auto nsec = end - start;
	return nsec.count();
}
void execute_three(SortFunc f, int n, ofstream& outF){
	long long b, a, w;
	int* arr = new int[n];
	generate_increasing_array(arr, n);
	b = execute_func(f, arr, n);
	generate_random_array(arr, n, RANDSEED);
	a = execute_func(f, arr, n);
	generate_decreasing_array(arr, n);
	w = execute_func(f, arr, n);
	outF << b << " " << a << " " << w << endl;
	delete[] arr;
	cout << "C";
}
void execute_sample(SortFunc f, int filename, long long maxminets, int range, int step) {

	int* arr = new int[2] {1, 2};
	//f(arr, 2);

	ofstream outF(MAINDIR + "\\" + to_string(filename)+".txt");
	long long max = maxminets * 60 * 1000000000;
	if (!outF) std::cerr << "Ошибка при открытии файла!" << std::endl;
	auto start = chrono::high_resolution_clock::now();
	for (int i = step; i <= range; i += step) {
		execute_three(f, i, outF);
		auto end = chrono::high_resolution_clock::now();
		auto span = end - start;
		
		if (span.count() > max) { cout << span.count(); break; }
	}
	outF.close();
}
int main() {
	auto samples = init();
	execute_sample(samples[0], 0, 4, RANGE, STEP);
	cout << "\nReady.\n";
	int i = 0;
	while (true) {
		auto samples = init();
		execute_sample(samples[i], i, MAXMIN, RANGE, STEP);
		cout << "\nAlg " << i + 1 << " ended.\n\n";
		i++;
	}
}