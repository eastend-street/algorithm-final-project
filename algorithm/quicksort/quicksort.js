// Create an array to sort
var array = [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11];
console.log(array);
document.write("<h2>Before sorting: " + array + "</h2>");

// Basic implementation (pivot is the first element of the array)
function quicksort(array) {
  if (array.length == 0) return [];

  var left = [],
    right = [],
    pivot = array[0];

  for (var i = 1; i < array.length; i++) {
    if (array[i] < pivot) left.push(array[i]);
    else right.push(array[i]);
  }

  return quicksort(left).concat(pivot, quicksort(right));
}

console.log(quicksort(array.slice())); // => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
document.write("<h2>After sorting: " + quicksort(array.slice()) + "</h2>");
