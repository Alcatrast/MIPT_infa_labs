#pragma once
namespace sortsamples {
    // 1. Пузырьковая сортировка
    void bubble_sort(int* array, int n) {
        for (int i = 0; i < n - 1; ++i) {
            for (int j = 0; j < n - i - 1; ++j) {
                if (array[j] > array[j + 1]) {
                    std::swap(array[j], array[j + 1]);
                }
            }
        }
    }

    // 2. Сортировка вставками
    void insertion_sort(int* array, int n) {
        for (int i = 1; i < n; ++i) {
            int key = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }

    // 3. Сортировка расческой (Comb Sort)
    void comb_sort(int* array, int n) {
        int gap = n;
        const float shrink = 1.3f; // Коэффициент уменьшения шага
        bool swapped = true;

        while (gap > 1 || swapped) {
            gap = static_cast<int>(gap / shrink);
            if (gap < 1) gap = 1; // Минимальный шаг

            swapped = false;

            for (int i = 0; i + gap < n; ++i) {
                if (array[i] > array[i + gap]) {
                    std::swap(array[i], array[i + gap]);
                    swapped = true;
                }
            }
        }
    }

    // 4. Сортировка выбором
    void selection_sort(int* array, int n) {
        for (int i = 0; i < n - 1; ++i) {
            int minIndex = i;
            for (int j = i + 1; j < n; ++j) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            std::swap(array[i], array[minIndex]);
        }
    }

    // 5. Быстрая сортировка
    namespace ATqss {
        void qs(int* s_arr, int first, int last)
        {
            int i = first, j = last, x = s_arr[(first + last) / 2];

            do {
                while (s_arr[i] < x) i++;
                while (s_arr[j] > x) j--;

                if (i <= j) {
                    if (s_arr[i] > s_arr[j]) {
                        int t = s_arr[i];
                        s_arr[i] = s_arr[j];
                        s_arr[j] = t;

                    }
                    i++;
                    j--;
                }
            } while (i <= j);

            if (i < last)
                qs(s_arr, i, last);
            if (first < j)
                qs(s_arr, first, j);
        }

    }
    void quick_sort(int* array, int n) {
        ATqss::qs(array, 0, n - 1);
    }

    //6. Сортировка слиянием
    namespace ATmss {
        void merge(int* array, int left, int mid, int right) {
            int n1 = mid - left + 1;
            int n2 = right - mid;

            int* L = new int[n1];
            int* R = new int[n2];

            for (int i = 0; i < n1; ++i)
                L[i] = array[left + i];
            for (int j = 0; j < n2; ++j)
                R[j] = array[mid + 1 + j];

            int i = 0, j = 0, k = left;
            while (i < n1 && j < n2) {
                if (L[i] <= R[j]) {
                    array[k++] = L[i++];
                }
                else {
                    array[k++] = R[j++];
                }
            }

            while (i < n1) {
                array[k++] = L[i++];
            }

            while (j < n2) {
                array[k++] = R[j++];
            }

            delete[] L;
            delete[] R;
        }

        void mergeSort(int* array, int left, int right) {
            if (left < right) {
                int mid = left + (right - left) / 2;
                mergeSort(array, left, mid);
                mergeSort(array, mid + 1, right);
                merge(array, left, mid, right);
            }
        }
    }
    void merge_sort(int* array, int n) {
        ATmss::mergeSort(array, 0, n - 1);
    }

    // 7. Сортировка кучей
    namespace AThss {
        void heapify(int* array, int n, int i) {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            if (left < n && array[left] > array[largest])
                largest = left;
            if (right < n && array[right] > array[largest])
                largest = right;
            if (largest != i) {
                std::swap(array[i], array[largest]);
                heapify(array, n, largest);
            }
        }
        void heapSort(int* array, int n) {
            for (int i = n / 2 - 1; i >= 0; --i)
                heapify(array, n, i);
            for (int i = n - 1; i > 0; --i) {
                std::swap(array[0], array[i]);
                heapify(array, i, 0);
            }
        }
    }
    void heap_sort(int* array, int n) {
        AThss::heapSort(array, n);
    }
}