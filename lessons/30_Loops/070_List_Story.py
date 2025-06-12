"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = ' '.join(words[:3:2]) + ' ' + ' '.join(words[7:10:2]) + ' ' + ' '.join(words[1:6:4]) + ' ' + ' '.join(words[13:16]) + ' ' + words[10] + ' ' + ' '.join(words[17:19])

# Create a story using the words in the list

# Display the story to the user
print(story)