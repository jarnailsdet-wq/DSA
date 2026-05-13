

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # --- PART 1: बेस केस और पॉइंटर सेटअप (Initialization) ---
        if not nums:
            return 0
        
        # 'i' वह जगह है जहाँ हम आखिरी unique नंबर रखते हैं
        i = 0 

        # --- PART 2: स्कैनिंग और अपडेटिंग (The Scanning Loop) ---
        for j in range(1, len(nums)):
            # अगर 'j' पर नया नंबर मिला जो 'i' वाले नंबर से अलग है
            if nums[j] != nums[i]:
                i += 1              # unique जगह को आगे बढ़ाएं
                nums[i] = nums[j]  # नए नंबर को वहाँ शिफ्ट करें

        # --- PART 3: फाइनल काउंट रिटर्न करना (Result) ---
        # कुल unique नंबर्स 'i + 1' होंगे क्योंकि index 0 से शुरू होता है
        return i + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    new_length = solution.removeDuplicates(nums)
    print(f"New length: {new_length}, Updated array: {nums[:new_length]}")