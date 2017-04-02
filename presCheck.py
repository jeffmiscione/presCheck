import tweepy   # linux:  sudo pip3 install tweepy // Windows:  pip install tweepy
import time
import serial

# Twitter API credentials ================================
consumer_key = "Q6iSleUN9MD6mRabru9RDwaM2"
consumer_secret = "ftEWSSzjctFygu4nTvhpzfesYXcM8SnNSbHmvJGhky3bCQnBMX"
access_key = "846797813224755200-Pp6FyA17Xnx8G2sk3N0IoTlCHE70T15"
access_secret = "1uI9poluFonQloi82Lzx5yJUf1T70NvntSvqt5ktrsUco"
twitter_target = 'JeffMiscione' # 'POTUS'
# ========================================================

# Functions ==============================================
def close_serial(serial_port):
    serial_port.close()
def get_most_recent_tweet(screen_name):
    # make initial request for most recent tweets (200 is the maximum allowed count)
    pres_tweets = api.user_timeline(screen_name=screen_name, count=1)

    return(pres_tweets[0].text)
def bash_head(serial_object):
    serial_object.write('b'.encode())
# ========================================================

# Setup ==================================================
# connect to arduino
port = "COM4" # /dev/ttyUSB0
connected = False
ser = serial.Serial(port, 9600)        # connects to the serial port

while not connected:
    serin = ser.read()
    print(serin.decode('ascii'))
    if serin.decode('ascii') == 'a':
        connected = True
        bash_head(ser)
    time.sleep(1)

print('connected')

# access Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
current_potus_tweet = get_most_recent_tweet(twitter_target)
# ========================================================

# Main Loop ==============================================
while True:
    new_tweet = get_most_recent_tweet(twitter_target)

    if(new_tweet != current_potus_tweet):
        bash_head(ser)
        current_potus_tweet = new_tweet

    time.sleep(5)