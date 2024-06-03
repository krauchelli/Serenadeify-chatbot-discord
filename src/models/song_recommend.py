# importing modules needed
import cv2 as cv
import pandas as pd

# declaring the variables needed
songCsv = '../../datasets/list_music.csv'

# reading csv file using pandas
songList = pd.read_csv(songCsv)

# dataframes and head
# songList = pd.DataFrame(songList)
# print(songList)
# songList.head()

# function to read get the recommendation
def getRecommendation(predictedY):
    # getting the index of the maximum value
    index = predictedY
    # filtered the song list based on the index
    songListFiltered = songList[songList['label'] == index]
    
    # random songs
    randomizedResult = songListFiltered.sample(n=5).reset_index(drop=True)
    
    listSong = []
    for i in range(len(randomizedResult)):
        songName = randomizedResult['track_name'][i]
        artist = randomizedResult['artists'][i]
        listSong.append((songName, artist))
        
    return listSong