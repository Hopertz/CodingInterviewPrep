# Array of Products

# O(n^2) time | O(n) space where n is the length of array.
def arrayOfProducts(array):
    product = []
    counter = 0
    while counter < len(array):
        running_prod = 1
        for indx in range(len(array)):
            if indx != counter:
                running_prod *= array[indx]

        product.append(running_prod)
        counter += 1

    return product


# Input array = [5, 1, 4, 2]
# Output [8, 40, 10, 20]
