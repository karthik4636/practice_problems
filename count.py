import os
count = 0
path, dirs, files = next(os.walk("/home/karthik/Desktop/interview_prep/practice_problems"))
for dir in ['trees','linked_list', 'arrays_and_strings',"sorting"]:
    path, dirs, files = next(
        os.walk(dir))
    print(dir, len(files))
    count+=len(files)

print(count)
