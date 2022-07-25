import pytube

url = input("Introduce un link: ")
video_a_descargar = pytube.YouTube(url)
print(video_a_descargar.title)
print(video_a_descargar.thumbnail_url)
video_a_descargar = video_a_descargar.streams.get_highest_resolution()
video_a_descargar.download()
print("Descargado")
