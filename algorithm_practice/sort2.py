house_count = int(input())
location = list(map(int, input().split()))
location.sort()

# get median location
print(location[(house_count -1)//2] )
