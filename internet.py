import speedtest
speed_test = speedtest.Speedtest()
download = speed_test.download()
upload = speed_test.upload()

download_mbps = round(download/10**6,2)
upload_mbps = round(upload/10**6,2)

print("Download Speed is : ",  download_mbps ," Mbps")
print("Upload Speed is :" , upload_mbps ,"Mbps")