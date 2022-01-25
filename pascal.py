import sys

def main():
    min = 0
    max = 0
    try:
        assert 2 <= len(sys.argv) <= 3
        if len(sys.argv) == 2:
            min = int(sys.argv[1])
            max = min
            assert min >= 0
        elif len(sys.argv) == 3:
            min = int(sys.argv[1])
            max = int(sys.argv[2])
            assert min >= 0 and max >= min
    except:
        print('bad command line!')
        return 1
    
    for n in range(min, max + 1):
        nums = []
        
        for i in range(0, n):
            nums += [1]
            newnums = [1]
            for j in range(0, len(nums) - 1):
                newnums += [nums[j] + nums[j + 1]]
            nums = newnums
        nums += [1]
        
        print(' '.join(str(n) for n in nums))
    return 0

if __name__ == '__main__':
    exit(main())
