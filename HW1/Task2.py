input_seconds = int(input())
seconds = input_seconds % 60
minutes = input_seconds // 60 % 60
hours = input_seconds // 3600
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
