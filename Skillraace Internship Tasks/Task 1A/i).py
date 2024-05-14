#i)Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in["Cricket","Ludo"].
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            print(sentence)