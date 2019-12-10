def getdata(place,key):
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={place}&key={key}'
    req = requests.get(url)
    try:
        if req.status_code == 200:
            data = req.json()
            place_id = data['results'][0]['place_id']
            place_name = data['results'][0]['name']
            photo_ref = data['results'][0]['photos'][0]['photo_reference']
            formated_add = data['results'][0]['formatted_address']
            #print('place_id = ',place_id)
            print('place_name = ',place_name)
            #print('photo_ref = ',photo_ref)
            #print('formated_add = ',formated_add)
            url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={key}'
            image = requests.get(url)
            if image.status_code == 200:
                with open('image.jpg','wb') as fp:
                    fp.write(image.content)
                    fp.close()
                plt.imshow(plt.imread('image.jpg'))
                plt.title(place_name,fontsize=20)
                plt.xlabel(formated_add,fontsize=20)
                plt.xticks([])
                plt.yticks([])
                plt.show()
            else:
                print('image is not found')
    except Exception as e:
        print('error plz check it out......',e)


if __name__=='__main__':
    import requests
    import json
    import matplotlib.pyplot as plt
    key = 'AIzaSyCNmQqNQd9xJKHTPtdoAnBi1LWxiJ96wUo'
    place = input('Enter a place name to search : ').replace(' ','%20').lower()
    getdata(place,key)
