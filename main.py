from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # 딕셔너리를 이용해 값을 저장
    num_map = {}
    
    # 배열의 각 요소에 대해 반복
    for i, num in enumerate(nums):
        complement = target - num
        
        # 목표값에서 현재 숫자를 뺀 값이 이미 딕셔너리에 있으면
        if complement in num_map:
            return [num_map[complement], i]
        
        # 현재 숫자를 딕셔너리에 추가
        num_map[num] = i

# 테스트 케이스 1
nums1 = [3, 2, 4]
target1 = 6
result1 = twoSum(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result1}")

# 테스트 케이스 2
nums2 = [3, 3]
target2 = 6
result2 = twoSum(nums2, target2)
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {result2}")

