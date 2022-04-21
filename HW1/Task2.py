input_seconds = int(input())
seconds = input_seconds % 60
minutes = input_seconds // 60 % 60
hours = input_seconds // 3600
print(f"{f'0{hours}' if hours < 10 else hours}:{f'0{minutes}' if minutes < 10 else minutes}:"
      f"{f'0{seconds}' if seconds < 10 else seconds}")
