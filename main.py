import bubble_sort as bbs
import selection_sort as ss
import insertion_sort as iss
import merge_sort as ms
import quick_sort as qs

if __name__ == "__main__":
    nums = [5, 3, 8, 6, 7, 2]
    # ss.sort(nums)
    # bbs.sort(nums)
    # iss.sort(nums)
    # ms.sort(nums)
    qs.sort(nums)
    print(nums)


