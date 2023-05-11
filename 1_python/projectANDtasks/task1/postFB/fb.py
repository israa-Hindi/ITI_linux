import facebook

# Set the access token to post request
access_token = 'EAASx8LZBd9KgBAC8Ljk1ttK8ZARzJHLvuy4YIvM9moT4g1B7BOHQ6qd7tTJi6U71GXoBne2qhw69RCo0NsrgBLSb9UZBxaa96ZAqy1BZB665n1IRpHVrDYak2cvTZAMf7kKiXscKRWn2iEPbwj3NWrpGvz189gFsHXK7lNKGX26dQRnZBplsIkf2cl3s0OsixjZBGz8CnwCu6mcYnbFkwDXF'
message = 'say Hi to my mewo!'

# Create a Facebook Graph API object
graph = facebook.GraphAPI(access_token)

# read pic 
with open('G:/lolo.jpg', 'rb') as image:
    image_data = image.read()
# pic id
photo_id = graph.put_photo(image_data, message=message)['id']

# Post the pic on your profile
graph.put_object("me", "feed",message=message,object_attachment=photo_id)

# # Post the message on your profile
# graph.put_object("me", "feed", message=message)

print('Just Give it time')