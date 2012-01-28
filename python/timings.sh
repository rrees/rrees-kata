echo "Selection (recursive)"
python -m timeit --repeat=3 'import sorting; import data; sorting.selection_sort(data.numbers)'

echo "Insertion sort"
python -m timeit --repeat=3 'import sorting; import data; sorting.insertion_sort(data.numbers)'

