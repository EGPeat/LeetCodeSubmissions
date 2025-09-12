class Solution:
    def bubbleSort(self, arr):
        swapped = False
        for i in range(len(arr) - 1):
            swapped = False
            for j in range(len(arr) - 1 - i):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
    def minimumBoxes(self, apples, boxCapacities):
        sum_apples = sum(apples)
        number_of_boxes = 0
        box_capacity = 0
        self.bubbleSort(boxCapacities)
        while box_capacity < sum_apples:
            box_capacity += boxCapacities[number_of_boxes]
            number_of_boxes += 1
        
        return number_of_boxes
