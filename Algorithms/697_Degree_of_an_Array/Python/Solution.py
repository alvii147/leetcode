class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # dictionary for storing occurrence information on each number
        num_occurrences = {}
        # maximum degree seen so far
        max_degree = 0
        # minimum sub array length seen so far
        min_sub_arr_len = len(nums)

        for i, num in enumerate(nums):
            if num in num_occurrences:
                num_occurrences[num]['last'] = i
                num_occurrences[num]['degree'] += 1
            else:
                num_occurrences[num] = {
                    'first': i,
                    'last': i,
                    'degree': 1,
                }

            # update maximum degree and minimum sub array seen so far
            degree = num_occurrences[num]['degree']
            sub_arr_len = num_occurrences[num]['last'] - num_occurrences[num]['first'] + 1
            if degree > max_degree or degree == max_degree and sub_arr_len <= min_sub_arr_len:
                max_degree = degree
                min_sub_arr_len = sub_arr_len

        return min_sub_arr_len
