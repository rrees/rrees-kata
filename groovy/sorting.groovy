data = [3, 7, 9, 12, 14, 3, 3, 5, 6]

def swap(array, i, j) {
    length = array.size()
    assert i < length
    assert j < length
    a = array.get(i)
    array[i] = array.get(j)
    array[j] = a
    return array
    }

for(i = 0; i < data.size(); i++) {
    println data.get(i)
    }
    
println swap(data, 2, 3)

def insertionSort(data) {
    for(i = 0; i < data.size(); i++) {
        for(j = i; i > 0 && j > 0 && (data[j] < data[j -1]); j--) {
            swap(data, j, j - 1)
         }
    }
    return data
}

def directInsertionSort(data) {
    for(i = 0; i < data.size(); i++) {
        for(j = i; i > 0 && j > 0 && (data[j] < data[j - 1]); j--) {
            if (data[j - 1] >= data[i]) {
                swap(data, i, j)
                }
         }
    }
    return data
}

println insertionSort(data)
println directInsertionSort(data)
println insertionSort([5,5,5])