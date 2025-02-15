####### Data Scrapping from Twitter

import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np


#########
#Part 1: Scrapping 5 coins
######## BITCOIN ########
key_word = "bitcoin"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2022-01-01" # Declare a start date
end_date = '2022-01-07'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_bitcoin.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")
#####################################################################################################
##### ETHEREUM #####

key_word = "ethereum"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2022-01-01" # Declare a start date
end_date = '2022-01-07'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_ethereum.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")
#####################################################################################################
##### CRYPTO #####

key_word = "crypto"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2022-01-01" # Declare a start date
end_date = '2022-01-07'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_crypto.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")
#####################################################################################################
##### DOGECOIN #####

key_word = "doge"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2022-01-01" # Declare a start date
end_date = '2022-01-07'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_doge.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")
#####################################################################################################
##### SHIBA INU #####

key_word = "shiba"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2022-01-01" # Declare a start date
end_date = '2022-01-07'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_shiba.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")
#####################################################################################################
##### Part 2: Bitcoin Surge and Crash #####

###### PRICE SURGE ######
#### Canada ####
key_word = "bitcoin"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2021-10-28" # Declare a start date
end_date = '2021-11-08'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en near:"Toronto" within:1000km'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_bitcoin_surge_canada.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")

#### US ####
key_word = "bitcoin"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2021-10-28" # Declare a start date
end_date = '2021-11-08'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en near:"Los Angeles" within:1000km'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_bitcoin_surge_usa.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")


############################################

##### PRICE CRASH #####
### Canada ###

key_word = "bitcoin"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2021-11-08" # Declare a start date
end_date = '2021-11-18'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en near:"Toronto" within:1000km'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_bitcoin_crash_canada.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")


### US ###
key_word = "bitcoin"  # Declare the key word used to search tweets
#user_name = "@mcgillu"   # Declare a user name used to search tweets
from_date = "2021-11-08" # Declare a start date
end_date = '2021-11-18'  # Declare a end date
count = 1000           # The maximum number of tweets
tweets_list_keyword = [] # A list used to store the returned results for keyword search
tweets_list_user = []    # A list used to store the retuned results for user search


#### Scraping tweets from a text search query ####
command_keyword = key_word+' lang:en near:"Los Angeles" within:1000km'+' since:'+from_date+' until:'+end_date # Define a string command for Scraper Api
print("Scraping data for keyword:",key_word)
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(command_keyword).get_items()):
    tweets_list_keyword.append([tweet.date,tweet.id, tweet.content, tweet.user.username, tweet.url]) # Append returned results to list
    if i>count:
        break;
# Create a dataframe from the tweets list above 
tweets_df_keyword = pd.DataFrame(tweets_list_keyword, columns=['Datetime','Tweet Id', 'Text', 'Username', 'url'])
tweets_df_keyword.to_csv("tweets_keyword_bitcoin_crash_usa.csv",index=False) # Export to a csv file
print("Scraped data have been exported to the csv file")


####################################################################
###### Import Modules
import snscrape.modules.twitter as sntwitter
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

#################################################################
###### Read Data and Preprocessing

df_surge_canada = pd.read_csv(r'C:\Users\Asus\Desktop\Text Analytics\Group Project\Scrapped Data\Toronto Los Angeles\tweets_keyword_bitcoin_surge_canada.csv')
df_surge_canada['Event'] = 'surge'
df_surge_canada['Country'] = 'Canada'


df_surge_usa = pd.read_csv(r'C:\Users\Asus\Desktop\Text Analytics\Group Project\Scrapped Data\Toronto Los Angeles\tweets_keyword_bitcoin_surge_usa.csv')
df_surge_usa['Event'] = 'surge'
df_surge_usa['Country'] = 'US'



df_crash_canada = pd.read_csv(r'C:\Users\Asus\Desktop\Text Analytics\Group Project\Scrapped Data\Toronto Los Angeles\tweets_keyword_bitcoin_crash_canada.csv')
df_crash_canada['Event'] = 'crash'
df_crash_canada['Country'] = 'Canada'


df_crash_usa = pd.read_csv(r'C:\Users\Asus\Desktop\Text Analytics\Group Project\Scrapped Data\Toronto Los Angeles\tweets_keyword_bitcoin_crash_usa.csv')
df_crash_usa['Event'] = 'crash'
df_crash_usa['Country'] = 'US'


df = pd.concat([df_surge_canada, df_surge_usa, df_crash_canada, df_crash_usa])
df = df[['Country','Event','Text','Datetime']]

#################################################################
###### Sentiment Analysis

SIA = SentimentIntensityAnalyzer()
sentiment_list = []
overall_sent = []

for sentence in df.Text:
    pol_sc = SIA.polarity_scores(sentence)
    sentiment_list.append(pol_sc)
    
df['Sentiment'] = sentiment_list
   
for i in sentiment_list:
    overall_sent.append(i['compound'])

df['overall_sentiment'] = overall_sent


df.to_csv("bitcoin_sentiment.csv",index=False) # Export to a csv file


###################################################################
###### Text Classification

from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("bitcoin_sentiment.csv")
df['sentiment'] = np.nan

for i in range(len(df['overall_sentiment'])):
    if df['overall_sentiment'][i] > 0:
        df['sentiment'][i] = 'Positive'
    if df['overall_sentiment'][i] < 0:
        df['sentiment'][i] = 'Negative'
    if df['overall_sentiment'][i] == 0:
        df['sentiment'][i] = 'Neutral'

tfvec = TfidfVectorizer(tokenizer=tokenize_text,stop_words=stopwords_nltk,decode_error='ignore')
tf_vectors = tfvec.fit_transform(df['Text'])

X_train, X_test, y_train, y_test = train_test_split(tf_vectors,
                                                    df['sentiment'],
                                                    test_size=0.25,
                                                    random_state=0)

y_train = np.asarray(y_train, dtype="|S6")
y_test = np.asarray(y_test, dtype="|S6")

## Trying different Naive Bayesian Classifiers

# MultinomialNB

MNB = MultinomialNB()
MNB.fit(X_train, y_train)

accuracy_MNB = accuracy_score(MNB.predict(X_test), y_test)
print('Accuracy score MNB: '+str('{:04.2f}'.format(accuracy_MNB*100))+'%')

# ComplementNB

CNB = ComplementNB()
CNB.fit(X_train, y_train)

accuracy_CNB = accuracy_score(CNB.predict(X_test), y_test)
print(str('Accuracy score CNB: '+'{:04.2f}'.format(accuracy_CNB*100))+'%')

# GaussianNB
# Note: This chunk of code takes significant amount of time to run

#GNB = GaussianNB()
#GNB.fit(X_train.todense(), y_train)

#accuracy_GNB = accuracy_score(GNB.predict(X_test), y_test)
#print(str('Accuracy score GNB: '+'{:04.2f}'.format(accuracy_GNB*100))+'%')

# BernoulliNB

BNB = BernoulliNB()
BNB.fit(X_train, y_train)

accuracy_BNB = accuracy_score(BNB.predict(X_test), y_test)
print(str('Accuracy score BNB: '+'{:04.2f}'.format(accuracy_BNB*100))+'%')

# Predicting a word with 'Positive' outcome
BNB.predict(tfvec.transform(['#bitcoin is the awesome!']))

# Predicting a word with 'Neutral' outcome
BNB.predict(tfvec.transform(['#bitcoin price is going up @ElonMusk']))

# Predicting a word 'Negative' outcome
# Note: I used a tweet example from the dataset. 
# The proportion of negative tweets are very small compared to the neutral and positive ones, 
# so the model tend to classify the words into one of those
BNB.predict(tfvec.transform(['#Bitcoin #SHIB #Ethereum IM NOT ALLOWED TO POST THIS VIDEO ANYMORE BUT I CAN QUOTE THIS TWEET LMAOOO 🤣🤣🤣YALL CANT STOP ME!!! THE ELITES WONT WIN, WE CAN WIN WE JUST NEED EVERYONE TO WAKE THE FUCK UP TO THEIR PLANS!!! BITCOIN IS THE ULTIMATE PRISON WE CANNOT ADOPT IT!!! #69 https://t.co/txzOXEWNuo']))
