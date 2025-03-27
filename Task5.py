try:
    file_path = '/Users/hugo/Documents/GitHub/VSMN20/text.txt'
    total_sum=0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                total_sum += float(line.strip())
            except ValueError:
                print(f"Could not convert {line} to a float")
    print(total_sum)
except FileNotFoundError:
    print("Could not find the file")
except Exception as e: 
    print(f"An error occured: {e}")
